#!/usr/bin/python

import re
import sys
import os.path
import csv
import datetime

__author__     = 'Upinder Sujlana'
__copyright__  = 'Copyright 2020, stMgr.log analysis & Data Analysis'
__version__    = '1.0.9'
__maintainer__ = 'Upinder Sujlana'
__email__      = ''
__status__     = 'prod'
#----------------------------------------------------------------------------------------------------
def getFileName():
    try:
        if sys.argv[1]:
            file_name=file_name=sys.argv[1]
    except:
        file_name="/var/log/springpath/stMgr.log"
        print ("No Filename provided, using the default  :- " + file_name)

    return file_name
#----------------------------------------------------------------------------------------------------
def getFileContents(file_name):
    tmp_list=[]
    try:
        with open(file_name) as file:
            tmp_list=[line.strip() for line in file]
    except Exception as e:
        print ( "getFileContents : A. Something bad happened.Please send your file and script details etc to Upinder Sujlana" )
        print ( str(e)  )

    try:
        no_empty = [x.strip() for x in tmp_list if x.strip()]
    except Exception as e:
        print ( "getFileContents : B. Something bad happened.Please send your file and script details etc to Upinder Sujlana" )
        print ( str(e)  )

    return no_empty
#----------------------------------------------------------------------------------------------------
def check_if_line_starts_with_date(line):
    if line is None:
        return False
    lll=list(line.strip())
    if not lll:
        return False
    if len(lll)<23:
        return False

    digitindex=[0, 1, 2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 22]
    charactersindex=[4,7,10,13,16,19]
    specialcharacter=['-',':','.']
    booleanindex=[]
    try:
        for i in digitindex:
            if lll[i]:
                booleanindex.append(lll[i].isdigit())
    except Exception as e:
        print ( "check_if_line_starts_with_date : A. Something bad happened.Please send your file and script details etc to Upinder Sujlana" )
        print ( str(e)  )
    try:
        for j in charactersindex:
            if lll[j]:
                booleanindex.append(lll[j] in specialcharacter)
    except Exception as e:
        print ( "check_if_line_starts_with_date : B. Something bad happened.Please send your file and script details etc to Upinder Sujlana" )
        print ( str(e)  )

    #Lets determine if all the criterias were met to confirm a date string. If not met than this is not a string that begins with date.
    if all(booleanindex):
        return True
    else:
        return False
#----------------------------------------------------------------------------------------------------
def createACraftylist(long_list):
    current_date_string=""
    scrappy=[]
    for i in long_list:
        if check_if_line_starts_with_date(i):
            scrappy.append(current_date_string)
            current_date_string=""
            current_date_string=i
        else:
            current_date_string=current_date_string + "\n" + i
    scrappy.append(current_date_string)

    scrappy_without_empty=[x.strip() for x in scrappy if x.strip()]

    try:
        if not scrappy_without_empty:
            print ("createACraftylist : Something bad happened.Please send your file and script details etc to Upinder Sujlana")
        else:
            return scrappy_without_empty
    except Exception, e:
        print >> sys.stderr, "Exception : createACraftylist : Something bad happened.Please send your file and script details etc to Upinder Sujlana"
        print >> sys.stderr, "Exception: %s" % str(e)
        sys.exit(1)

    return scrappy_without_empty
#----------------------------------------------------------------------------------------------------
def createListOfTuples(filetolist):
    listOfTuples = []
    try:
        for str1 in filetolist:
            if str1.strip():
                mo = re.search(r'(\d{4}\-\d{2}\-\d{2}\-\d{2}\:\d{2}\:\d+\.\d+)\s+(\[.*\])\s+(\[.*\])\s+(\[.*\])\s+([A-Z]+)\s+(.+)\s+\-\s+(.*)',str1,flags=re.MULTILINE | re.DOTALL)
                listOfTuples.append( ( mo.group(1) , mo.group(5), mo.group(7) ) )
    except Exception as e:
        print ( "createListOfTuples : Something bad happened.Please send your file and script details etc to Upinder Sujlana" )
        print ( str(e)  )

    return listOfTuples
#----------------------------------------------------------------------------------------------------
def main():

    file_name = getFileName()

    filetolist = []
    if file_name:
        filetolist =  getFileContents(file_name)

    long_list    =  createACraftylist(filetolist)
    listOfTuples =  createListOfTuples(long_list)

    if listOfTuples:
        print ("Writing a stmgr_dump_*.csv file in the /tmp directory")
        filename = datetime.datetime.now()
        csv_filename="/tmp/stmgr_dump_"+filename.strftime("%Y_%B_%d-%H:%M:%S")+ ".csv"
        with open(csv_filename,'wb') as out:
            csv_out=csv.writer(out)
            csv_out.writerow(['Datetime','Message Severity', 'Message Text'])
            for row in listOfTuples:
                csv_out.writerow(row)
#----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
