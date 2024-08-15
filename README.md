# red-canary-sdk-python

## Example Usage

```
from rcapi import rcapi
url = 'https://demo.my.redcanary.co/'
key = 'put_key_here'

connection = rcapi(url=url, key=key)

# list all detections
results = connection.detection.get_list()

# Get THREAT-123
print(connection.detection.get_item(123))

# Get EVT-12234
print(connection.event.get_item(12234))

# List Automate playbooks
print(connection.automate.list_playbooks())
```

There are two ways to get an object:

```
from rcapi import rcapi
from rcapi.models import Detection

# personal portal API key
api_key = "ASDFASDFASDFASDFASDFASDF"
# domain
domain = "demo"

connection = rcapi(url=f"https://{domain}.my.redcanary.co",api_key=api_key)

# Using the "Detection" model
Detection.get_item(connection, unique_id: 123)
Detection.get_list(connection)

# Using the callable functions of the connection
connection.detection.get(123)
connection.detection.list_detections()
```
