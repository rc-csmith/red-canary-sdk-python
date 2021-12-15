from RCAPI.services import automate
from RCAPI.models.common import BaseObject
from RCAPI.client import Client

class RCAPI():
  """
  Usage:
  from RCAPI import RCAPI
  
  rc = RCAPI(url="demo.my.redcanary.co",key="asdfasdf")
  """

  def __init__(self, url, key):
    self.base_url = url.rstrip('/')
    self.headers = {"X-Api-Key": "{0}".format(key)}
    self.client = Client(self.base_url, self.headers)

    #self.detection = detection.Detections(self.client)
    #self.activity_monitor = activity_monitor.ActivityMonitors(self.client)
    #self.audit_log = audit_log.AuditLogs(self.client)
    #self.tactic_technique = tactic_technique.TacticTechnique(self.client)
    self.automate = automate.Automate(self.client)
  
  def TestConnection(self):
    temp = self.client.get(service='/automate/configuration')

    if isinstance(temp, BaseObject):
      return True
    else:
      return False