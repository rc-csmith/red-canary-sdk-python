import requests
import json

class Client(object):
  def __init__(self, url, headers):
    self.base_url = url
    self.headers = headers

  def get(self, service, api_prefix='/openapi/v3'): # TODO: support pagination
    url = self.base_url + api_prefix + service
    response = requests.get(url, headers=self.headers)
    
    if response.status_code == 200:
      return json.loads(response.content.decode('utf-8'))
    else:
      raise Exception('Error! Status code error {0}'.format(response.status_code))

  def patch(self, service, params, api_prefix='/openapi/v3'): 
    url = self.base_url + api_prefix + service
    response = requests.patch(url, headers=self.headers, data=params)

    if response.status_code == 200:
      return json.loads(response.content.decode('utf-8'))
    else:
      raise Exception('Error! Status code error {0}'.format(response.status_code))

  def post(self, service, params, api_prefix='/openapi/v3'): 
    url = self.base_url + api_prefix + service
    response = requests.post(url, headers=self.headers, data=params)

    if response.status_code == 200:
      return json.loads(response.content.decode('utf-8'))
    else:
      raise Exception('Error! Status code error {0}'.format(response.status_code))
  
  def delete(self, service, params, api_prefix='openapi/v3'):
    url = self.base_url + api_prefix + service
    response = requests.delete(url, headers=self.headers)

    if response.status_code == 200:
      return json.loads(response.content.decode('utf-8'))
    else:
      raise Exception('Error! Status code error {0}'.format(response.status_code))