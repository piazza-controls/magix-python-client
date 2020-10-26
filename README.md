[![Build Status](https://travis-ci.org/waltz-controls/magix-python-client.svg?branch=main)](https://travis-ci.org/waltz-controls/magix-python-client)
[![PyPI version](https://badge.fury.io/py/magix-client.svg)](https://badge.fury.io/py/magix-client)

# magix-python-client

Python client implementation for Magix, see [RFC-2](https://github.com/waltz-controls/rfc/tree/master/2)

## Usage

```
pip install magix_client
```

```python
magix_host = 'http://magix:8080'

#create instance
client = MagixHttpClient(magix_host)
#
client.observe().subscribe(lambda event: print(json.loads(event.data)))
client.broadcast({'hello':'world'})
```
