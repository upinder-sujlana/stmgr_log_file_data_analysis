### stmgr_log_file_data_analysis
```
Wrote the python script to scrap through stMgr.log logfile. The file has log lines e.g.

2020-04-01-18:00:02.685 [] [] [ForkJoinPool-1-worker-13] DEBUG com.storvisor.sysmgmt.util.Utils$ - validationToOption: Value Obtained: HostSystem:host-517 @ https://sdkTunnel:8089/sdk
2020-04-01-18:00:02.685 [] [opId=5dfc80ae7de9a993, operationId=5dfc80ae7de9a993.5dfc80ae7de9a993<:5dfc80ae7de9a993] [pool-2-thread-13] DEBUG c.s.s.v.VirtPlatformImpl$ - Attempting to get virtDatastore info: HX-2 on hosts: ParVector(HostSystem:ha-host @ https://172.16.67.140/sdk, HostSystem:host-527 @ https://sdkTunnel:8089/sdk, HostSystem:host-517 @ https://sdkTunnel:8089/sdk, HostSystem:host-524 @ https://sdkTunnel:8089/sdk)
2020-04-01-18:00:02.688 [] [opId=5dfc80ae7de9a993, operationId=5dfc80ae7de9a993.5dfc80ae7de9a993<:5dfc80ae7de9a993] [New I/O worker #9] DEBUG c.s.sysmgmt.stMgr.StMgrImpl$ - getClusterUncached: platClusterRaw HxCluster(EntityRef(384ebbe8a108b3f8:55f0c2f2e5a9e339,Cluster,None,None,None),StPlatformClusterConfig(Some(192.168.5.145),Some(4),Some(384ebbe8a108b3f8:55f0c2f2e5a9e339),Some(ThreeCopies),Some(Lenient),None,Some(Unknown),None,Some(DefaultCluster)),Online,Healthy,1579306765,66253128676147,22084376225382,251816225450,21832559999932,Set(EntityRef(24882605564dc557:02365387d997f082,Pnode,Some(192.168.5.143),None,None), EntityRef(f36ac5a7564d1742:720686a30e8aa2c3,Pnode,Some(192.168.5.142),None,None), EntityRef(967a1334564d4796:b6b9a86a42c7f385,Pnode,Some(192.168.5.141),None,None), EntityRef(cd840f56564d1d8d:543d4371ae9a5b96,Pnode,Some(192.168.5.144),None,None)),Some(Compliant),Some(Map(NodeFailuresToReadonly -> 3, HddFailuresToShutdown -> 3, HddFailuresTolerable -> 2, SsdFailuresToReadonly -> NA, NumNodesUnavailable -> 0, MetadataCopiesRemaining -> 3, DataCopiesRemaining -> 3, NodeFailuresTolerable -> 1, HddFailuresToReadonly -> 3, SsdFailuresTolerable -> 2, HealthReason -> Storage cluster is healthy.
, NodeFailuresToEnospaceWarn -> NA, TimeToFinishHealingInSecs -> , SsdFailuresToShutdown -> 3, CacheCopiesRemaining -> 3, NodeFailuresToShutdown -> 3, EnsembleSize -> 4, HealingStatus -> )),Some(4),Some(1424740),Some(0),Some(HxClusterResiliencyInfo(Healthy,1,2,2,Some(ArrayBuffer(Storage cluster is healthy. )),None)),Some(HxClusterHealingInfo(false,None,None,None)),Some(false))
2020-04-01-18:00:02.688 [] [opId=5dfc80ae7de9a993, operationId=5dfc80ae7de9a993.5dfc80ae7de9a993<:5dfc80ae7de9a993] [New I/O worker #9] DEBUG c.s.s.c.z.m.ZKStatusManager - Checking if ZK leader/follower for host: 192.168.5.144


The idea is to pickup all lines that begin with the date (loglines run multiple new lines)
and convert the log file into a CSV.

The script will pickup at this time three critical things from a log line:

- Date

- Message Severity level

- Message Text

Running script
----------------
root@SpringpathController2KM:/tmp# chmod +x stmgrToCSV_ver9.py
root@SpringpathController2KM:/tmp# python stmgrToCSV_ver9.py
No Filename provided, using the default  :- /var/log/springpath/stMgr.log
Writing a stmgr_dump_*.csv file in the /tmp directory
root@SpringpathController7K1NFXL2KM:/tmp#

This dumps a file in the /tmp folder e.g. stmgr_dump_2020_April_02-13:21:41.csv

After that I used the the generated  CSV file for analysis using Pandas. The Jupyter notebook is attached with notes.


```
