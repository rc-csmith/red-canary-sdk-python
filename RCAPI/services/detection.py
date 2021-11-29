from RCAPI.models.detection import Detection, UpdateRemedatedStatus, Summary, Detector, IOC
#from RCAPI.models.detection import IOC

class Detection(object):
  def __init__(self, client):
    self.client = client

  def list(self):
    results = []
    array = self.client.get('/detections').get('data')

    for item in array:
      results.append(Detection(item))

    return results

  def list_marked_iocs(self, type=['all']):
    type_list = ['file','regkey','domain','ip','all']

    results = []
      
    array = self.client.get('/detections/marked_indicators_of_compromise').get('data')

    for item in array:
      if 'all' in type:
        results.append(IOC(item))
      else:
        for thing in type:
          if thing not in type_list:
            raise Exception("Error! Type {0} not supported".format(thing))
          else:
            if IOC(item)._type == thing:
              results.append(IOC(item))
    return results
  
  def list_summaries(self):
    results = []
    array = self.client.get('/detections/summary').get('data')

    for item in array:
      results.append(Summary(item))

    return results

  def download(self):
    return self.client.get('/detections/request_csv')
  
  def list_detection_events(self, detection_id): #TODO: Figure out data model for Events
    return self.client.get('/detections/{0}/events'.format(detection_id))
  
  def list_detection_marked_iocs(self, detection_id, type=['all']):
    type_list = ['file','regkey','domain','ip','all']
    results = []
    array = (self.client.get('/detections/{0}/marked_indicators_of_compromise'.format(detection_id))).get('data')
  
    for item in array:
      if 'all' in type:
        results.append(IOC(item))
      else:
        for thing in type:
          if thing not in type_list:
            raise Exception ("Error! Type {0} not supported".format(thing))
          else:
            if IOC(item)._type == thing:
              results.append(IOC(item))
    return results
  
  def update_remedation_status(self, detection_id, remediation_info):
    params = remediation_info.to_json()

    return self.client.patch(service='/detections/{0}/update_remediation_state'.format(detection_id),params=params)

  def mark_acknowledged(self, detection_id):
    return self.client.patch('/detections/{0}/mark_acknowledged'.format(detection_id))

  def get(self, detection_id):
    return Detection((self.client.get('/detections/{0}'.format(detection_id))).get('data'))
  
  def list_timeline(self, detection_id): #TODO: Figure out data model for timeline
    return self.client.get('/detections/{0}/timeline'.format(detection_id))

  def list_detectors(self, detection_id):
    results = []
    array = self.client.get('/detections/{0}/detectors'.format(detection_id))  

    for item in array:
      results.append(Detector(item))
    
    return results

  def list_related(self, detection_id):
    results = []
    array = self.client.get('/detections/{0}/related_detections'.format(detection_id)).get('data')

    for item in array:
      results.append(Detection(item))

    return results

  def download_tactic(self):
    return self.client.get('/reports/detections_by_observed_tactic/request_csv')
  
  def download_technique(self):
    return self.client.get('/reports/detections_by_observed_technique/request_csv')
