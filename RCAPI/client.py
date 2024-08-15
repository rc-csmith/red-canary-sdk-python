"""
Client for rcapi
"""
import os
from datetime import datetime
import json
import requests
import time
import logging
from typing import Optional, Union, Any, Tuple, Generator
from .models.general import StandardErrorResponse
from .models.common import BaseObject, Resource, Collection, SelectableObject

class Client(object):
  """
  Client class for rcapi
  """
  def __init__(self, url, headers):
    self.session = requests.Session()
    self.session.headers.update(headers)
    self.base_url = url

    logging.Formatter.converter = time.gmtime
    os.makedirs(os.path.abspath('./logs/'), exist_ok=True)
    logging.basicConfig(filename=os.path.abspath(f'./logs/{datetime.utcnow().strftime("%Y%m%d%H%M%S")}_rcapi.log'), 
                        level=logging.DEBUG, format='[%(asctime)s] [%(levelname)-8s] [%(name)-36s] [%(filename)-20s:%(lineno)-4s] %(message)s')

  def call_api(self, method: str, service: str, object_type=BaseObject, params: Optional[dict]=None, api_prefix: str='/openapi/v3', retry_limit: int = 1) -> None:
    if hasattr(self, method) and callable(func := getattr(self, method)):
      logging.debug(f"Calling service {service} with parms {params}")
      result = func(service=service, object_type=object_type, params=params, api_prefix=api_prefix)

      # Go through a retry loop if there are 429 errors since it means the API key has been rate limited
      if isinstance(result, StandardErrorResponse) and hasattr(result, 'code') and result.code == 429:
        counter = 0
        wait_counter = 3
        while isinstance(result, StandardErrorResponse) and hasattr(result, 'code') and result.code == 429 and counter != retry_limit:
          time.sleep(wait_counter ** (counter + 1))
          counter += 1
          logging.debug(f"Received response error {result.code}. Retry #{counter} for service {service}")
          result = func(service=service, object_type=object_type, params=params, api_prefix=api_prefix)

      if isinstance(result, StandardErrorResponse):
        logging.error(result.to_json())

      return result
    else:
      raise ValueError(f"Request method {method} not supported")

  def get(self, service: str, object_type=BaseObject, params: Optional[dict]=None, api_prefix: str='/openapi/v3') -> Union[BaseObject, StandardErrorResponse]:
    """
    Get requests
    """
    url = self.base_url + api_prefix + service    

    response = self.session.get(url, data=params)

    if response.ok:
      if issubclass(object_type, SelectableObject) or issubclass(object_type, Resource) or issubclass(object_type, Collection):
        return object_type(json.loads(response.content.decode('utf-8')), self)
      else:
        try:
          return object_type(json.loads(response.content.decode('utf-8')))
        except:
          return object_type(response.content.decode('utf-8'))
    else:
      try:
        return StandardErrorResponse(json.loads(response.content.decode('utf-8')))
      except:
        return StandardErrorResponse({'web_content':response.content.decode('utf-8'), 'code': response.status_code})

  def put(self, service: str, object_type=BaseObject, params: Optional[dict]=None, api_prefix: str='/openapi/v3') -> Union[BaseObject, StandardErrorResponse]:
    """
    Put requests
    """
    url = self.base_url + api_prefix + service
    response = self.session.put(url, data=params)

    if response.ok:
      if issubclass(object_type, SelectableObject) or issubclass(object_type, Resource) or issubclass(object_type, Collection):
        return object_type(json.loads(response.content.decode('utf-8')), self)
      else:
        return object_type(json.loads(response.content.decode('utf-8')))
    else:
      try:
        return StandardErrorResponse(json.loads(response.content.decode('utf-8')))
      except:
        return StandardErrorResponse({'web_content':response.content.decode('utf-8')})

  def patch(self, service: str, object_type=BaseObject, params: Optional[dict]=None, api_prefix: str='/openapi/v3') -> Union[BaseObject, StandardErrorResponse]:
    """
    Patch requests
    """
    url = self.base_url + api_prefix + service
    response = self.session.patch(url, data=params)

    if response.ok:
      if issubclass(object_type, SelectableObject) or issubclass(object_type, Resource) or issubclass(object_type, Collection):
        return object_type(json.loads(response.content.decode('utf-8')), self)
      else:
        return object_type(json.loads(response.content.decode('utf-8')))
    else:
      try:
        return StandardErrorResponse(json.loads(response.content.decode('utf-8')))
      except:
        return StandardErrorResponse({'web_content':response.content.decode('utf-8')})

  def post(self, service: str, object_type=BaseObject, params: Optional[dict]=None, api_prefix: str='/openapi/v3') -> Union[BaseObject, StandardErrorResponse]:
    """
    Post requests
    """
    url = self.base_url + api_prefix + service
    response = self.session.post(url, data=params)

    if response.ok:
      if issubclass(object_type, SelectableObject) or issubclass(object_type, Resource) or issubclass(object_type, Collection):
        return object_type(json.loads(response.content.decode('utf-8')), self)
      else:
        return object_type(json.loads(response.content.decode('utf-8')))
    else:
      try:
        return StandardErrorResponse(json.loads(response.content.decode('utf-8')))
      except:
        return StandardErrorResponse({'web_content':response.content.decode('utf-8')})

  def delete(self, service: str, object_type=BaseObject, params: Optional[dict]=None, api_prefix: str='/openapi/v3') -> Union[BaseObject, StandardErrorResponse]:
    """
    Delete requests
    """
    url = self.base_url + api_prefix + service
    response = self.session.delete(url, data=params)

    if response.ok:
      if issubclass(object_type, SelectableObject) or issubclass(object_type, Resource) or issubclass(object_type, Collection):
        return object_type(json.loads(response.content.decode('utf-8')), self)
      else:
        return object_type(json.loads(response.content.decode('utf-8')))
    else:
      try:
        return StandardErrorResponse(json.loads(response.content.decode('utf-8')))
      except:
        return StandardErrorResponse({'web_content':response.content.decode('utf-8')})

  def CheckRequiredKeys(self, required_keys: list[str], params: dict, function_name: str) -> None:
    """
    Check if required keys are present
    """
    for item in required_keys:
      if item not in params:
        raise Exception(f"Error! Key {item} not in provided parameters for {function_name}")
  
  def CheckCountMode(self, count_mode: bool, object_type) -> Tuple[dict, Any]:
    """
    Check if extra parms are needed
    """

    params = {'count_mode':'true'} if count_mode else {}
    final_object_type = BaseObject if count_mode else object_type

    return params, final_object_type

  def RecurseList(self, service: str, object_type=BaseObject, params:dict={}, total_items: Optional[int]=None) -> Union[Generator, dict, BaseObject]:
    """
    Recursive get request
    """
    results: list = []
    params['page'] = 1
    temp = self.call_api('get', service, object_type, params)
    # ensure we do not submit more than one request every 1 second to comply with rate limit
    last_request = time.time()

    if isinstance(temp, object_type): #Verify initial call is successful
      total_items = temp.total_items if hasattr(temp, 'total_items') else total_items #Not all collections have a total_items attribute

      if total_items is not None:
        num_of_results = len(results)
      elif hasattr(temp, 'data'):
        num_of_results = len(temp.data)
      else:
        return temp
      
      while self._if_statement(num_of_results, total_items):
        for item in temp.data:
          yield item
        params['page'] += 1

        if time.time() - last_request < 1:
          time.sleep(1)
        temp = self.call_api('get', service, object_type, params)
        last_request = time.time()
        if not isinstance(temp, object_type): #Verify all subsequent calls are successful
          return temp
      
        num_of_results = len(results) if total_items is not None else len(temp.data)
    else:
      return temp
  
  def _if_statement(self, num_of_results: int, total_items: Optional[int]) -> bool:
    if total_items is None:
      return bool(num_of_results)
    else:
      return bool(num_of_results < total_items)