from RCAPI.models.audit_log import Audit_Log

class AuditLog(object):
  def __init__(self, client):
    self.client = client

  def list(self):
    results = []
    array = self.client.get('/audit_logs')

    for item in array:
      results.append(Audit_Log(item))
    
    return results

  def download(self):
    return self.client.get('/audit_logs/request_csv')

  def get(self, audit_log_id):
    return Audit_Log(self.client.get('/audit_logs/{0}'.format(audit_log_id)))