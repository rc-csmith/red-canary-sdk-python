from RCAPI.models.exec import *
from RCAPI.services.common import CheckRequiredKeys

class Automate(object):
  def __init__(self, client):
    self.client = client

  def remove_trigger_playbook(self, playbook_id, trigger_id): #Return success or failure
    return (self.client.delete('/automate/triggers/{0}/playbooks?playbook[id]={1}'.format(trigger_id, playbook_id), object_type=PlaybookResource))
  
  def add_trigger_playbook(self, trigger_id, params={}): #Return success or failure
    required_keys = ['playbook[id]']
    CheckRequiredKeys(required_keys, params, 'add_trigger_playbook')

    return (self.client.post(service='/automate/triggers/{0}/playbooks'.format(trigger_id), params=params, object_type=PlaybookResource))
  
  def delete_trigger_condition(self, trigger_id, condition_id): #Return success or failure
    return TriggerConditionCollection(self.client.delete('/automate/triggers/{0}/conditions/{1}'.format(trigger_id, condition_id)))
  
  def create_trigger_condition(self, trigger_id, params={}): #Return success or failure
    required_keys = ['condition[model]','condition[attribute_name]','condition[matcher]','condition[value]']
    CheckRequiredKeys(required_keys, params, 'create_trigger_condition')

    return (self.client.post(service='/automate/triggers/{0}/conditions'.format(trigger_id), params=params, object_type=TriggerConditionResource))
  
  def list_trigger_conditions(self, trigger_id): #Return array of TriggerConditions
    return (self.client.get(service='/automate/triggers/{0}/conditions'.format(trigger_id), object_type=TriggerConditionCollection))
  
  def update_trigger(self, trigger_id, params={}): #Return contents if success, errors if failure
    required_keys = ['trigger[id]']
    CheckRequiredKeys(required_keys, params, 'update_trigger')

    return (self.client.patch(service='/automate/triggers/{0}'.format(trigger_id), params=params, object_type=TriggerResource))

  def delete_trigger(self, trigger_id): #Return success or failure
    return (self.client.delete(service='/automate/triggers/{0}'.format(trigger_id), object_type=TriggerResource))
  
  def create_trigger(self, params={}): #Return contents if success, errors if failure
    required_keys = ['trigger[trigger]']
    CheckRequiredKeys(required_keys, params, "create_trigger")

    return (self.client.post(service="/automate/triggers", params=params, object_type=TriggerResource))
  
  def list_triggers(self): #To return array of Triggers
    results = []
    page = 1
    temp = (self.client.get(service='/automate/triggers?page={0}'.format(page), object_type=TriggerCollection))

    while len(temp.data) != 0:
      for item in temp.data:
        results.append(item)
      page += 1
      temp = self.client.get(service='/automate/triggers?page={0}'.format(page), object_type=TriggerCollection)
    return results

  def delete_playbook_action(self, playbook_id, action_id): #Return success or failure
    return (self.client.delete(service='/automate/playbooks/{0}/actions/{1}'.format(playbook_id, action_id), object_type=PlaybookActionResource))
  
  def update_playbook_action(self, playbook_id, action_id, params={}): #Return contents if success, errors if failure
    return (self.client.patch(service='/automate/playbooks/{0}/actions/{1}'.format(playbook_id, action_id), params=params, object_type=PlaybookActionResource))
  
  def create_playbook_action(self, playbook_id, params={}): #Return success or failure
    required_keys = ['action[type]','action[row_order]']
    CheckRequiredKeys(required_keys, params, 'create_playbook_action')

    return (self.client.post(service='/automate/playbooks/{0}/actions'.format(playbook_id),params=params, object_type=PlaybookResource))
  
  def copy_playbook(self, playbook_id): #Return contents if success, errors if failure
    return (self.client.post(service='/automate/playbooks/{0}'.format(playbook_id), object_type=PlaybookResource))
  
  def delete_playbook(self, playbook_id): #Return success or failure
    return (self.client.delete(service='/automate/playbooks/{0}'.format(playbook_id), object_type=PlaybookResource))
  
  def update_playbook(self, playbook_id, params={}): #Return contents if success, errors if failure
    required_keys = ['playbook[id]']
    CheckRequiredKeys(required_keys, params, 'update_playbook')
  
    return (self.client.patch(service='/automate/playbooks/{0}'.format(playbook_id), params=params, object_type=PlaybookResource))
  
  def create_playbook(self, params={}): #Return contents if success, errors if failure
    return (self.client.post(service='/automate/playbooks', params=params, object_type=PlaybookResource))
  
  def list_playbooks(self): #Return array of Playbooks
    results = []
    page = 1
    temp = (self.client.get('/automate/playbooks?page={0}'.format(page), object_type=PlaybookCollection))

    if isinstance(temp, PlaybookCollection): #Verify initial call is successful
      while len(temp.data) != 0:
        for item in temp.data:
          results.append(item)
        page += 1
        temp = (self.client.get('/automate/playbooks?page={0}'.format(page), object_type=PlaybookCollection))
        if not isinstance(temp,PlaybookCollection): #Verify all subsequent calls are successful
          return temp
      return results
    else:
      return temp