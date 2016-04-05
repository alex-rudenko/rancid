#!/usr/bin/python
import time
import shutil
from subprocess import call

#Open Rancid.conf file, hardcoded, change if needed !!!
rancid = open('/etc/rancid/rancid.conf', 'r')

regions=[]
flag=0

# From rancid.conf extract path to SVN (basepath)
# and subfolgers list in str format (reg_src)
for ln in rancid:
    if 'LIST_OF_GROUPS=' in ln:
        if '$LIST_OF_GROUPS' not in ln:
            reg_src=ln
    line = ln.split()
    if 'BASEDIR=' in line[0]:
      basepath = line[0][8:-1]

#Transform (reg_src) to extract subfolders as array to store in regions[]
reg_src=reg_src.replace('"',' " ')
reg_split=reg_src.split()

#Make subfolders (regions) array
for reg in reg_split:
    if reg=='"': flag=flag+1
    if flag==1 and reg!='"': regions.append(reg)

#Set timestamp to destination folder
timestamp=time.strftime("%Y%m%d-%H%M%S")

#Copy configs&router.db to destination folder
for reg in regions:
    confsrc=basepath+'/'+reg+'/configs'
    rdbsrc=basepath+'/'+reg+'/router.db'
    confdst='/backup-rancid/'+timestamp+'/'+reg+'/configs'
    rdbdst='/backup-rancid/'+timestamp+'/'+reg+'/router.db'
    shutil.copytree(confsrc,confdst) 
    shutil.copy2(rdbsrc,rdbdst)

#Create TAR.GZ Archive with backup files
cmd="tar -zcf /backup-rancid/"+timestamp+".tar.gz -C /backup-rancid/ "+timestamp
call(cmd.split())

#Cleanup
cmd="rm -rf /backup-rancid/"+timestamp+"/"
call(cmd.split())

#Close Rancid.conf file
rancid.close()
