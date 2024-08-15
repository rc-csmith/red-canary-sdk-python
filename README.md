# red-canary-sdk-python

## Example Usage

```
from RCAPI import RCAPI
url = 'https://demo.my.redcanary.co/'
key = 'put_key_here'

connection = RCAPI(url=url, key=key)

# list all detections
results = connection.detection.list()

# Get THREAT-123
print(connection.detection.get(123))

# Get EVT-12234
print(connection.event.get(12234))

# List Automate playbooks
print(connection.automate.list_playbooks())
```

There are two ways to get an object:

```
from RCAPI import RCAPI
from RCAPI.models import Detection

# personal portal API key
api_key = "ASDFASDFASDFASDFASDFASDF"
# domain
domain = "demo"

connection = RCAPI(url=f"https://{domain}.my.redcanary.co",api_key=api_key)

# Using the "Detection" model
Detection.get_item(connection, unique_id: 123)
Detection.get_list(connection)

# Using the callable functions of the connection
connection.detection.get(123)
connection.detection.list_detections()
```
