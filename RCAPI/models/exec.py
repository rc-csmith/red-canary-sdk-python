"""
Exec
"""
from typing import Union, Optional
from .general import PortalUser, Indicator, StandardSuccessResponse, StandardErrorResponse
from .common import SelectableObject, BaseObject, Resource, Collection

class PlaybookAction(BaseObject):
  """
  Playbook Action object
  Includes Indicator
  """
  def __init__(self, entry=None, client=None):
    if entry['indicator'] is not None:
      type_mapping = {
        'indicator': Indicator
      }
    else:
      type_mapping = {}

    if client:
      self.client = client

    if entry:
      super().__init__(entry, type_mapping)
  
  def update(self, params: Optional[dict]=None):
    """
    Update current playbook action
    
    Parameters
    ----------
    params : dict
      dictionary containing attributes for playbook action
    """
    try:
      return Automate(self.client).update_playbook_action(self.playbook_id, self.id, params)
    except Exception as e:
      raise SyntaxError(e)

class Playbook(SelectableObject):
  """
  Playbook object
  Includes PlaybookAction
  """
  def __init__(self, entry=None, client=None):
    type_mapping = {
      "actions": PlaybookAction
    }

    if client:
      self.client = client

    if entry:
      super().__init__(entry, type_mapping)
  
  def get_list(self):
    """
    Get a list of playbooks
    """
    if hasattr(self,'client'):
      return Automate(self.client).list_playbooks()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")

  def get_item(self, unique_id: str):
    """
    Get a single playbook

    Parameters
    ----------
    unique_id : str
      unique id for the playbook
    """
    if hasattr(self,'client'):
      temp_list = Automate(self.client).list_playbooks()
      for item in temp_list:
        if str(item.id) == unique_id:
           return item
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")
    
  def create_item(self, params: Optional[dict]=None):
    """
    Create playbook

    Parameters
    ----------
    params : dict
      dictionary containing attributes for playbook
    """
    if hasattr(self,'client'):
      return Automate(self.client).create_playbook(params)
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to create a new item")
    
  def update(self, params: dict):
    """
    Update current playbook

    Parameters
    ----------
    params : dict
      dictionary containing attributes for playbook
    """
    try:
      return Automate(self.client).update_playbook(self.id, params)
    except Exception as e:
      raise SyntaxError(e)
  
  def delete(self):
    """
    Delete current playbook
    """
    try:
      return Automate(self.client).delete_playbook(self.id)
    except Exception as e:
      raise SyntaxError(e)
  
  def copy(self):
    """
    Copy current playbook
    """
    try:
      return Automate(self.client).copy_playbook(self.id)
    except Exception as e:
      raise SyntaxError(e)

  def add_action(self, params: dict):
    """
    Add action to current playbook
    
    Parameters
    ----------
    params : dict
      dictionary containing attributes for action
    """
    try:
      return Automate(self.client).create_playbook_action(self.id, params)
    except Exception as e:
      raise SyntaxError(e)
  
  def remove_action(self, action: PlaybookAction):
    """
    Remove action from current playbook
    
    Parameters
    ----------
    action : PlaybookAction
      PlaybookAction object
    """
    try:
      return Automate(self.client).delete_playbook_action(self.id, action.id)
    except Exception as e:
      raise SyntaxError(e)
  
  def list_actions(self):
    """
    List actions for current playbook
    """
    try:
      return self.actions
    except Exception as e:
      raise SyntaxError(e)

class TriggerCondition(BaseObject):
  """
  Trigger Condition object
  """

class Trigger(SelectableObject):
  """
  Trigger object
  Includes TriggerCondition
  """
  def __init__(self, entry=None, client=None):
    type_mapping = {
      'conditions': TriggerCondition
    }
    if client:
      self.client = client

    if entry:
      super().__init__(entry, type_mapping)
  
  def get_list(self):
    """
    Get a list of triggers
    """
    if hasattr(self,'client'):
      return Automate(self.client).list_triggers()
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to generate a list")

  def get_item(self, unique_id: str):
    """
    Get a single trigger
    
    Parameters
    ----------
    unique_id : str
      unique id for the trigger
    """
    if hasattr(self,'client'):
      temp_list = Automate(self.client).list_triggers()
      for item in temp_list:
        if str(item.id) == unique_id:
          return item
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to get an item")

  def create_item(self, params: dict):
    """
    Create trigger

    Parameters
    ----------
    params : dict
      dictionary containing attributes for trigger
    """
    if hasattr(self,'client'):
      return Automate(self.client).create_trigger(params)
    else:
      raise SyntaxError(f"Class {self.__class__.__name__} cannot be used to create a new item")

  def update(self, params: dict):
    """
    Update current trigger
    
    Parameters
    ----------
    params : dict
      dictionary containing attributes for trigger
    """
    try:
      return Automate(self.client).update_trigger(self.id, params)
    except Exception as e:
      raise SyntaxError(e)

  def delete(self):
    """
    Delete current trigger
    """
    try:
      return Automate(self.client).delete_trigger(self.id)
    except Exception as e:
      raise SyntaxError(e)
  
  def list_conditions(self):
    """
    List conditions for current trigger
    """
    try:
      return Automate(self.client).list_trigger_conditions(self.id)
    except Exception as e:
      raise SyntaxError(e)

  def add_condition(self, params: dict):
    """
    Add condition to current trigger
    
    Parameters
    ----------
    params : dict
      dictionary containing attributes for condition
    """
    try:
      return Automate(self.client).create_trigger_condition(self.id, params)
    except Exception as e:
      raise SyntaxError(e)
  
  def remove_condition(self, condition: TriggerCondition):
    """
    Remove condition from current trigger
    
    Parameters
    ----------
    condition : TriggerCondition
      TriggerCondition object
    """
    try:
      return Automate(self.client).delete_trigger_condition(self.id, condition.id)
    except Exception as e:
      raise SyntaxError(e)
  
  def add_playbook(self, playbook: Playbook):
    """
    Attach playbook to current trigger
    
    Parameters
    ----------
    playbook : Playbook
      Playbook object
    """
    try:
      return Automate(self.client).add_trigger_playbook(self.id, {'playbook[id]': playbook.id})
    except Exception as e:
      raise SyntaxError(e)

  def remove_playbook(self, playbook: Playbook):
    """
    Detach playbook from current trigger
    
    Parameters
    ----------
    playbook : Playbook
      Playbook object
    """
    try:
      return Automate(self.client).remove_trigger_playbook(self.id, playbook.id)
    except Exception as e:
      raise SyntaxError(e)

class PlaybookExecution(BaseObject):
  """
  Playbook Execution object
  Includes Playbook, Trigger, and PortalUser
  """
  def __init__(self, entry):
    type_mapping = {
      'playbook': Playbook,
      'trigger': Trigger,
      'executing_user': PortalUser
    }
    super().__init__(entry, type_mapping)

class PlaybookExecutionResource(Resource):
  """
  Playbook Execution resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, PlaybookExecution, client=client)

class ActionExecution(BaseObject):
  """
  Action Execution object
  Includes PlaybookAction, PortalUser, PlaybookExecution, and Playbook
  """
  def __init__(self, entry):
    type_mapping = {
      'action': PlaybookAction,
      'approved_by': PortalUser,
      'denied_by': PortalUser,
      'playbook_execution': PlaybookExecution,
      'playbook': Playbook
    }
    super().__init__(entry, type_mapping)

class ActionExecutionResource(Resource):
  """
  Action Execution resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, ActionExecution, client=client)

class ActionExecutionCollection(Collection):
  """
  Action Execution collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, ActionExecution, client=client)

class PlaybookResource(Resource):
  """
  Playbook resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, Playbook, client=client)

class TriggerConditionCollection(Collection):
  """
  Trigger Condition collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, TriggerCondition, client=client)

class TriggerConditionResource(Resource):
  """
  Trigger Condition resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, TriggerCondition, client=client)

class TriggerResource(Resource):
  """
  Trigger resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, Trigger, client=client)

class TriggerCollection(Collection):
  """
  Trigger collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, Trigger, client=client)

class PlaybookActionResource(Resource):
  """
  Playbook Action resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, PlaybookAction, client=client)

class PlaybookCollection(Collection):
  """
  Playbook collection object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, Playbook, client=client)

class InterpolationResponse(BaseObject):
  """
  Interpolation Response object
  """

class Configuration(BaseObject): #TODO: Undefined objects here
  """
  Configuration object
  """

class ConfigurationResource(Resource):
  """
  Configuration resource object
  """
  def __init__(self, entry, client=None):
    super().__init__(entry, Configuration, client=client)

class Automate(object):
  """
  Automate class
  """
  def __init__(self, client):
    self.client = client

  def test_json(self, params: Optional[dict] = None) -> InterpolationResponse:
    """
    Check if JSON is formatted properly

    Parameters
    ----------
    params : dict
      dictionary containing json string to be tested and accessor
      required keys: json_str
                     accessor
    """
    required_keys = ['json_str','accessor']
    self.client.CheckRequiredKeys(required_keys,params,'test_json')

    return self.client.call_api(method='post',service='/automate/test_json_interpolation',params=params,object_type=InterpolationResponse)

  def remove_trigger_playbook(self, playbook_id: int, trigger_id: int) -> Union[StandardSuccessResponse, StandardErrorResponse]:
    """
    Detach playbook from trigger

    Parameters
    ----------
    playbook_id : int
      playbook id
    trigger_id: int
      trigger id
    """
    result = self.client.call_api(method='delete',service=f'/automate/triggers/{trigger_id}/playbooks?playbook[id]={playbook_id}',
                              object_type=PlaybookResource)
    
    if isinstance(result, PlaybookResource):
      return StandardSuccessResponse({"msg":"Playbook successfully detached from trigger."})
    else:
      return result
 
  def add_trigger_playbook(self, trigger_id: int, params: dict) -> Playbook:
    """
    Attach playbook to trigger

    Parameters
    ----------
    trigger_id : int
      trigger id
    params : dict
      dictionary containing playbook id and other attributes
      required keys: playbook[id]
    """
    required_keys = ['playbook[id]']
    self.client.CheckRequiredKeys(required_keys, params, 'add_trigger_playbook')

    result = self.client.call_api(method='post',service=f'/automate/triggers/{trigger_id}/playbooks',
                            params=params, object_type=PlaybookResource)
  
    try:
      return result.data[0]
    except:
      return result

  def delete_trigger_condition(self, trigger_id: int, condition_id: int) -> Union[StandardSuccessResponse, StandardErrorResponse]:
    """
    Delete trigger condition

    Parameters
    ----------
    trigger_id : int
      trigger id
    condition_id : int
      condition id
    count_mode : bool
      show only a count and omit result details
    """

    result = self.client.call_api(method='delete',service=f'/automate/triggers/{trigger_id}/conditions/{condition_id}', object_type=TriggerConditionResource)

    if isinstance(result, TriggerConditionResource):
      return StandardSuccessResponse({"msg":"Trigger condition successfully deleted"})
    else:
      return result

  def create_trigger_condition(self, trigger_id: int, params: dict) -> TriggerCondition:
    """
    Create condition for specified trigger

    Parameters
    ----------
    trigger_id : int
      trigger id
    params : dict
      dictionary containing attributes of condition
      required keys: condition[model]
                     condition[attribute_name]
                     condition[matcher]
                     condition[value] OR condition[value][]
    """
    required_keys = ['condition[model]','condition[attribute_name]','condition[matcher]']

    if isinstance(params, list):
      adjusted_params = []
      for array in params:
        adjusted_params.append(array[0])
    else:
      adjusted_params = params

    #CheckRequiredKeys doesn't support "either/or" logic checks so we have to do this here
    if not ('condition[value]' in adjusted_params or 'condition[value][]' in adjusted_params):
      raise Exception("Error! Neither key condition[value][] nor key condition[value] \
                      in provided parameters for create_trigger_condition")

    self.client.CheckRequiredKeys(required_keys, adjusted_params, 'create_trigger_condition')

    result = self.client.call_api(method='post',service=f'/automate/triggers/{trigger_id}/conditions',
                            params=params, object_type=TriggerConditionResource)
  
    try:
      return result.data[0]
    except:
      return result

  def list_trigger_conditions(self, trigger_id: int, count_mode: bool = False) -> Union[int, list[TriggerCondition]]:
    """
    List conditions for trigger

    Parameters
    ----------
    trigger_id : int
      trigger id
    count_mode : bool
      show only a count and omit result details
    """
    
    params, object_type = self.client.CheckCountMode(count_mode, TriggerConditionCollection)

    if count_mode:
      return self.client.call_api(method='get',service=f'/automate/triggers/{trigger_id}/conditions', object_type=object_type, params=params)
    else:
      return self.client.RecurseList(service=f'/automate/triggers/{trigger_id}/conditions', object_type=object_type, params=params)

  def update_trigger(self, trigger_id: int, params: dict) -> Trigger:
    """
    Update existing trigger

    Parameters
    ----------
    trigger_id : int
      trigger id
    params : dict
      dictionary containing details for trigger
      required keys: trigger[id]
    """
    required_keys = ['trigger[id]']
    self.client.CheckRequiredKeys(required_keys, params, 'update_trigger')

    result = self.client.call_api(method='patch',service=f'/automate/triggers/{trigger_id}',
            params=params, object_type=TriggerResource)
    
    try:
      return result.data[0]
    except:
      return result

  def delete_trigger(self, trigger_id: int) -> Union[StandardSuccessResponse, StandardErrorResponse]:
    """
    Delete trigger

    Parameters
    ----------
    trigger_id : int
      trigger id
    """
    result = self.client.call_api(method='delete',service=f'/automate/triggers/{trigger_id}', object_type=TriggerResource)

    if isinstance(result, TriggerResource):
      return StandardSuccessResponse({"msg":"Trigger successfully deleted"})
    else:
      return result

  def create_trigger(self, params: dict) -> Trigger:
    """
    Create trigger
    
    Parameters
    ----------
    params : dict
      dictionary containing attributes for trigger
      required keys: trigger[trigger]
    """
    required_keys = ['trigger[trigger]']
    self.client.CheckRequiredKeys(required_keys, params, "create_trigger")

    result = self.client.call_api(method='post',service="/automate/triggers", params=params, object_type=TriggerResource)

    try:
      return result.data[0]
    except:
      return result

  def list_triggers(self, count_mode: bool = False) -> Union[int, list[Trigger]]:
    """
    List all triggers

    Parameters
    ----------
    count_mode : bool
      show only a count and omit result details
    """

    params, object_type = self.client.CheckCountMode(count_mode, TriggerCollection)

    if count_mode:
      return self.client.call_api(method='get',service='/automate/triggers', object_type=object_type, params=params)
    else:
      return self.client.RecurseList(service='/automate/triggers', object_type=object_type, params=params)

  def get_playbook_action_runtime_attributes(self, playbook_id: int, action_id: int, runtime_attributes: int) -> dict:
    """
    Get runtime attributes for playbook action

    Parameters
    ----------
    playbook_id : int
      playbook id
    action_id : int
      action id
    runtime_attributes : int
      runtime attributes
    """
    return self.client.call_api(method='get',service=f'/automate/playbooks/{playbook_id}/actions/{action_id}/{runtime_attributes}',
                            object_type=dict)

  def delete_playbook_action(self, playbook_id: int, action_id: int) -> Union[StandardErrorResponse, StandardSuccessResponse]:
    """
    Delete action from playbook

    Parameters
    ----------
    playbook_id : int
      playbook id
    action_id : int
      action id
    """
    result = self.client.call_api(method='delete',service=f'/automate/playbooks/{playbook_id}/actions/{action_id}',
                              object_type=PlaybookActionResource)
    
    if isinstance(result, PlaybookActionResource):
      return StandardSuccessResponse({"msg":"PlaybookAction successfully deleted"})
    else:
      return result

  def update_playbook_action(self, playbook_id: int, action_id: int, params: Optional[dict]=None) -> PlaybookAction:
    """
    Update action in playbook
    
    Parameters
    ----------
    playbook_id : int
      playbook id
    action_id : int
      action id
    params : dict
      dictionary of attributes for action
    """
    result = self.client.call_api(method='patch',service=f'/automate/playbooks/{playbook_id}/actions/{action_id}',
                             params=params, object_type=PlaybookActionResource)
  
    try:
      return result.data[0]
    except:
      return result

  def create_playbook_action(self, playbook_id: int, params: dict) -> PlaybookAction:
    """
    Create action for playbook

    Parameters
    ----------
    playbook_id : int
      playbook id
    params : dict
      dictionary of action attributes
      required keys: action[type]
                     action[row_order]
    """
    required_keys = ['action[type]','action[row_order]']
    self.client.CheckRequiredKeys(required_keys, params, 'create_playbook_action')

    result = self.client.call_api(method='post',service=f'/automate/playbooks/{playbook_id}/actions',
                                  params=params, object_type=PlaybookActionResource)
  
    try:
      return result.data[0]
    except:
      return result

  def get_playbook_execution_actions(self, playbook_id: int, execution_id: int) -> list[ActionExecution]:
    """
    Get actions for playbook execution
    
    Parameters
    ----------
    playbook_id : int
      playbook id
    execution_id : int
      execution id
    """

    return self.client.RecurseList(service=f'/automate/playbooks/{playbook_id}/executions/{execution_id}/actions',
                                   object_type=ActionExecutionCollection)

  def get_playbook_execution(self, playbook_id: int, execution_id: int) -> PlaybookExecution:
    """
    Get playbook execution

    Parameters
    ----------
    playbook_id : int
      playbook id
    execution_id : int
      execution id
    """
    return self.client.call_api(method='get',service=f'/automate/playbooks/{playbook_id}/executions/{execution_id}',
                            object_type=PlaybookExecutionResource)
  

  def list_playbook_execution(self, playbook_id: int) -> list[PlaybookExecution]:
    """
    List playbook executions

    Parameters
    ----------
    playbook_id : int
      playbook id
    """
    return self.client.RecurseList(service=f'/automate/playbooks/{playbook_id}/executions', object_type=PlaybookExecutionResource)

  def list_playbook_action_history(self, playbook_id: int) -> Playbook:
    """
    List playbook action history

    Parameters
    ----------
    playbook_id : int
      playbook id
    """
    return self.client.call_api(method='get',service=f'/automate/playbooks/{playbook_id}/action_history', object_type=PlaybookResource)

  def list_playbook_history(self, playbook_id: int) -> Playbook:
    """
    List playbook history

    Parameters
    ----------
    playbook_id : int
      playbook id
    """
    return self.client.call_api(method='get',service=f'/automate/playbooks/{playbook_id}/history', object_type=PlaybookResource)

  def copy_playbook(self, playbook_id: int) -> Playbook:
    """
    Make copy of existing playbook

    Parameters
    ----------
    playbook_id : int
      playbook id
    """
    result = self.client.call_api(method='post',service=f'/automate/playbooks/{playbook_id}', object_type=PlaybookResource)

    try:
      return result.data[0]
    except:
      return result

  def delete_playbook(self, playbook_id: int) -> Playbook:
    """
    Delete playbook

    Parameters
    ----------
    playbook_id : int
      playbook id
    """
    result = self.client.call_api(method='delete',service=f'/automate/playbooks/{playbook_id}', object_type=PlaybookResource)

    if isinstance(result, PlaybookResource):
      return StandardSuccessResponse({"msg":"Playbook successfully deleted"})
    else:
      return result

  def update_playbook(self, playbook_id: int, params: dict) -> Playbook:
    """
    Update playbook

    Parameters
    ----------
    playbook_id : int
      playbook id
    params : dict
      dictionary of playbook attributes
      required_keys : playbook[id]
    """
    required_keys = ['playbook[id]']
    self.client.CheckRequiredKeys(required_keys, params, 'update_playbook')

    result = self.client.call_api(method='patch',service=f'/automate/playbooks/{playbook_id}', params=params, object_type=PlaybookResource)

    try:
      return result.data[0]
    except:
      return result

  def create_on_demand_playbook(self, detection_id: int, indicator_id: list[int], action: list[str]) -> Playbook:
    """
    Create on-demand playbook
    
    Parameters
    ----------
    detection_id : int
      detection id
    indicator_id : list[int]
      list of indicator ids
    action : list[str]
      list of actions
    """

    params = {
      'detection_id': detection_id,
      'actions[indicator_id]': indicator_id,
      'actions[action]': action
    }

    result = self.client.call_api(method='post',service='/automate/playbooks/on_demand', params=params, object_type=PlaybookResource)

    try:
      return result.data[0]
    except:
      return result

  def create_playbook(self, name: str = None, description: str = None) -> Playbook:
    """
    Create playbook

    Parameters
    ----------
    name : str
      name of playbook
    description : str
      description of playbook
    """
    params = {}

    if name:
      params['playbook[name]'] = name
    if description:
      params['playbook[description]'] = description

    result = self.client.call_api(method='post',service='/automate/playbooks', params=params, object_type=PlaybookResource)

    try:
      return result.data[0]
    except:
      return result

  def list_playbooks(self) -> Union[int, list[Playbook]]:
    """
    List all playbooks
    """
  
    return self.client.RecurseList(service='/automate/playbooks', object_type=PlaybookCollection)

  def get_configuration(self) -> Configuration:
    """
    Get configuration
    """
    return self.client.call_api(method='get',service='/automate/configuration', object_type=ConfigurationResource)
  
  def deny_action_execution(self, playbook_id: int) -> ActionExecution:
    """
    Deny action execution

    Parameters
    ----------
    playbook_id : int
      playbook id
    """
    return self.client.call_api(method='post',service=f'/automate/action_executions/{playbook_id}/deny', object_type=ActionExecutionResource)
  
  def approve_action_execution(self, playbook_id: int) -> ActionExecution:
    """
    Approve action execution

    Parameters
    ----------
    playbook_id : int
      playbook id
    """
    return self.client.call_api(method='post',service=f'/automate/action_executions/{playbook_id}/approve', object_type=ActionExecutionResource)
  
  def get_action_execution(self, action_execution_id: int, exclude_playbook: bool = False, exclude_playbook_execution: bool = False, exclude_playbook_available_actions: bool = False) -> ActionExecution:
    """
    Get action execution

    Parameters
    ----------
    action_execution_id : int
      action execution id
    exclude_playbook : bool
      exclude playbook
    exclude_playbook_execution : bool
      exclude playbook execution
    exclude_playbook_available_actions : bool
      exclude playbook available actions
    """
    query = []

    if exclude_playbook:
      query.append('exclude_playbook=true')
    if exclude_playbook_execution:
      query.append('exclude_playbook_execution=true')
    if exclude_playbook_available_actions:
      query.append('exclude_playbook_available_actions=true')

    full_query = '?' + '&'.join(query) if query else ''

    return self.client.call_api(method='get',service=f'/automate/action_executions/{action_execution_id}{full_query}', object_type=ActionExecutionResource)
