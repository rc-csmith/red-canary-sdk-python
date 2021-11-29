from RCAPI.models.activity_monitor import Activity_Monitor, NewActivityMonitor, Match

class ActivityMonitor(object):
  def __init__(self, client):
    self.client = client

  def create(self, activity_monitor):
    params = activity_monitor.to_json()

    return self.client.post(service='/activity_monitors',params=params)
  
  def list(self):
    results = []
    array = self.client.get('/activity_monitors').get('data')

    for item in array:
      results.append(Activity_Monitor(item))
    
    return results
  
  def list_matches(self, activity_monitor_id): 
    return Match(self.client.get('/activity_monitors/{0}/matches'.format(activity_monitor_id)).get('data'))
  
  def deactivate(self, activity_monitor_id):
    return self.client.delete('/activity_monitors/{0}'.format(activity_monitor_id))

  def get(self, activity_monitor_id):
    return Activity_Monitor(self.client.get('/activity_monitors/{0}'.format(activity_monitor_id)).get('data'))

  def list_all_matches(self):
    results = []
    array = self.client.get('/activity_monitor_matches').get('data')

    for item in array:
      results.append(Match(item))

    return results
  
  def list_all_file_integrity_matches(self): #TODO: Figure out model for file integrity matches
    return self.client.get('/activity_monitor_matches/file_integrity_monitoring_matches/json')
  
  def download_all_file_integrity_matches(self):
    return self.client.get('activity_monitor_matches/file_integrity_monitoring_matches/csv')
    