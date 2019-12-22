
![PyPI](https://img.shields.io/pypi/v/damn-simple-jsonrpc-server-django.svg)
![Downloads](https://pepy.tech/badge/damn-simple-jsonrpc-server-django)
![Coverage Status](https://coveralls.io/repos/github/marcinn/json-rpc-server-django/badge.svg?branch=master)


# JSON RPC-Server adaptor for Django

This is a Django adaptor for
(Damn Simple JSON RPC Server)[https://github.com/marcinn/json-rpc-server/]

## Compatibility

- Django 1.11
- Django 2.x
- Django 3.x

# Installation


```
pip install damn-simple-jsonrpc-server-django
```

## Configure Django project

Add `jsonrpcdjango` to `INSTALLED_APPS`

(settings.py)
```python
INSTALLED_APPS = [
    # ...
    'jsonrpcdjango'
]
```

Expose services in `urlpatterns`:


(urls.py)
```python
from django.conf.urls import patterns, include, url
from calculator_service import calculator

urlpatterns = patterns('',
        url(r'^$', 'jsonrpcdjango.serve', kwargs={'service':
        calculator},
                    name='calculator'),
                    )
```
