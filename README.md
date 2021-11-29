# red-canary-sdk-python

## Example Usage

from RCAPI import RCAPI

```
url = 'https://demo.my.redcanary.co/'
key = 'put_key_here'

connection = RCAPI(url=url, key=key)

results = connection.detection.list()
```