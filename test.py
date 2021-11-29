import os
import subprocess
import json
from RCAPI import RCAPI
#from RCAPI.services.detection import Detection
#from RCAPI.models.activity_monitor import NewActivityMonitor
#from RCAPI.models.detection import UpdateRemedatedStatus

def pull_api_key():
  if os.path.exists('/bin/zsh'): #In case you're working with an older macOS
    exec = "/bin/zsh"
  else:
    exec = "/bin/bash"

  x = (subprocess.run("security find-generic-password -w -s 'RC_API_KEY' -a 'user'",shell=True,executable=exec,capture_output=True).stdout).decode("utf8").replace("\n","")

  if x == '':
    print("Service 'RC_API_KEY' with account 'user' not set up in keychain. Best practice is to set up your API key in the keychain rather than the zsh profile. Will fall back and use environment variable RC_API_KEY.")
  else:
    return x

url = 'https://demo.my.redcanary.co/'
key = pull_api_key()

connection = RCAPI(url=url, key=key)

results = connection.activity_monitor.list_all_file_integrity_matches()

print(results)
#temp = UpdateRemedatedStatus(remediation_state='remediated')

#connection.update_remedation_status(detection_id='153',remediation_info=temp)

#temp = NewActivityMonitor(name='Name',type='file_modification',active=True,file_modification_types_monitored='filedeletion',file_paths_monitored='/bin/ssh')

#print(temp.to_json())