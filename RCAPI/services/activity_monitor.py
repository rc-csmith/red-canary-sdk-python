from RCAPI.models.activity_monitor import Activity_Monitor, NewActivityMonitor

class ActivityMonitor(object):
  def __init__(self, client):
    self.client = client

  def create(self, activity_monitor):
    params = activity_monitor.to_json()

    return self.client.post(service='/activity_monitors',params=params)
  
  def list(self):
    return self.client.get('/activity_monitors')
  
  def list_matches(self, activity_monitor_id):
    return self.client.get('/activity_monitors/{0}/matches'.format(activity_monitor_id))
  
  def deactivate(self, activity_monitor_id):
    return self.client.delete('/activity_monitors/{0}'.format(activity_monitor_id))

  def get(self, activity_monitor_id):
    return self.client.get('/activity_monitors/{0}'.format(activity_monitor_id))

  def list_all_matches(self):
    return self.client.get('/activity_monitor_matches')
  
  def list_all_file_integrity_matches(self):
    return self.client.get('/activity_monitor_matches/file_integrity_monitoring_matches/json')
  
  def download_all_file_integrity_matches(self):
    return self.client.get('activity_monitor_matches/file_integrity_monitoring_matches/csv')
    