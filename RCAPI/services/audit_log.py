from RCAPI.models.audit_log import AuditLog

class AuditLog(object):
  def __init__(self, client):
    self.client = client

  def list(self):
    return self.client.get('/audit_logs')
  
  def download(self):
    return self.client.get('/audit_logs/request_csv')

  def get(self, audit_log_id):
    return self.client.get('/audit_logs/{0}'.format(audit_log_id))