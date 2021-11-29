from RCAPI.models.tactic_technique import Tactic_Technique, RelatedTechnique

class TacticTechnique(object):
  def __init__(self, client):
    self.client = client
  
  def get_tactic(self, tactic_id):
    return Tactic_Technique(self.client.get('/detectors/attack_tactics/{0}'.format(tactic_id)).get('data'))
  
  def list_tactics(self):
    results = []
    array = self.client.get('/detectors/attack_tactics').get('data')

    for item in array:
      results.append(Tactic_Technique(item))
    
    return results

  def get_technique(self, technique_id):
    return Tactic_Technique(self.client.get('/detectors/attack_techniques/{0}'.format(technique_id)).get('data'))
  
  def list_techniques(self):
    results = []
    array = self.client.get('/detectors/attack_techniques').get('data')
  
    for item in array:
      results.append(Tactic_Technique(item))
    
    return results
    