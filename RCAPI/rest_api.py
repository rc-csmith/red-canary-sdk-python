from .services import detection, activity_monitor, audit_log
from RCAPI.client import Client

class RCAPI():
  """
  Usage:
  from rcapi import RCAPI
  
  rc = RCAPI(url="demo.my.redcanary.co",key="asdfasdf")
  """

  def __init__(self, url, key):
    self.base_url = url.rstrip('/')
    self.headers = {"Content-Type": "application/json", "X-Api-Key": "{0}".format(key)}
    self.client = Client(self.base_url, self.headers)
    self.detection = detection.Detection(self.client)
    self.activity_monitor = activity_monitor.ActivityMonitor(self.client)
    self.audit_log = audit_log.AuditLog(self.client)