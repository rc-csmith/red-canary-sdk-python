from RCAPI.models.tactic_technique import TacticTechnique, RelatedTechnique

class TacticTechnique(object):
  def __init__(self, client):
    self.client = client
  
  def get_tactic(self, tactic_id):
    return self.client.get('/detectors/attack_tactics/{0}'.format(tactic_id))
  
  def list_tactics(self):
    return self.client.get('/detectors/attack_tactics')
  
  def get_technique(self, technique_id):
    return self.client.get('/detectors/attack_techniques/{0}'.format(technique_id))
  
  def list_techniques(self):
    return self.client.get('/detectors/attack_techniques')