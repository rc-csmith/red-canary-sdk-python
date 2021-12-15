import requests
import json
from RCAPI.models.exec import *
from RCAPI.models.general import StandardErrorResponse
from RCAPI.models.common import BaseObject

class Client(object):
  def __init__(self, url, headers):
    self.base_url = url
    self.headers = headers

  def get(self, service, object_type=BaseObject, api_prefix='/openapi/v3'): # TODO: support pagination
    url = self.base_url + api_prefix + service
    response = requests.get(url, headers=self.headers)
    
    if response.ok:
      return object_type(json.loads(response.content.decode('utf-8')))
    else:
      return StandardErrorResponse(json.loads(response.content.decode('utf-8')))

  def patch(self, service, object_type=BaseObject, params=None, api_prefix='/openapi/v3'): 
    url = self.base_url + api_prefix + service
    response = requests.patch(url, headers=self.headers, data=params)

    if response.ok:
      return object_type(json.loads(response.content.decode('utf-8')))
    else:
      return StandardErrorResponse(json.loads(response.content.decode('utf-8')))

  def post(self, service, object_type=BaseObject, params=None, api_prefix='/openapi/v3'): 
    url = self.base_url + api_prefix + service
    response = requests.post(url, headers=self.headers, data=params)

    if response.ok:
      return object_type(json.loads(response.content.decode('utf-8')))
    else:
      return StandardErrorResponse(json.loads(response.content.decode('utf-8')))
  
  def delete(self, service, object_type=BaseObject, params=None, api_prefix='openapi/v3'):
    url = self.base_url + api_prefix + service
    response = requests.delete(url, headers=self.headers)

    if response.ok:
      return object_type(json.loads(response.content.decode('utf-8')))
    else:
      return StandardErrorResponse(json.loads(response.content.decode('utf-8')))
