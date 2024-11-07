# red-canary-sdk-python

## Installation & Setup

1. Download a copy of this repo
2. From the root of the repo directory, run the following command
```bash
pip install ./rcapi
```
1. Set environment variables or pass as optional parameters to the `rcapi` object:
```bash
RED_CANARY_CUSTOMER_ID=<YOUR CUSTOMER ID/NAME>
RED_CANARY_AUTH_TOKEN=<YOUR API TOKEN>
```

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

# Using the object model
Detection.get_item(connection, unique_id: 123)
Detection.get_list(connection)

# Using the callable functions of the connection
connection.detection.get(123)
connection.detection.list_detections()
```

## Architecture
- All objects have the `.to_json()` function that can convert the custom object to non-empty JSON format.
- Object models that support callable functions (e.g. `get_item`, `create`, etc.) are listed below. For a full list of callable functions for each object, see the [documentation](./docs/).
  - ActivityMonitor
  - ActivityMonitorMatch
  - AttackTactic
  - AttackTechnique
  - AuditLog
  - Detection
  - Endpoint
  - EndpointUser
  - Event
  - ExternalAlert
  - ExternalAlertSourcePlatform
  - ExternalService
  - FileIntegrityMatch
  - IgnoredTargetedProduct
  - ManagedPortalUser
  - Playbook
  - PortalRole
  - Report
  - ReportingTag
  - ReportingTagAssociation
  - SharedFile
  - SuppressionRule
  - TargetedProduct
  - Trigger
