
![PyPI](https://img.shields.io/pypi/v/damn-simple-jsonrpc-server-django.svg)
![Downloads](https://pepy.tech/badge/damn-simple-jsonrpc-server-django)
![Coverage Status](https://coveralls.io/repos/github/marcinn/json-rpc-server-django/badge.svg?branch=master)


# JSON RPC-Server adaptor for Django

This is a Django adaptor for
[Damn Simple JSON RPC Server](https://github.com/marcinn/json-rpc-server/)

## Compatibility

- Django 2.x, Python 3.8
- Django 3.x/4.x, Python 3.9/3.10
- Django 4.x/5.0, Python 3.10/3.11/3.12
- Django 5.1/5.2, Python 3.10/3.11/3.12/3.13

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
from django.urls import path
from jsonrpcdjango import serve
from calculator_service import calculator

urlpatterns = [
    path('', serve, {'service': calculator}, name='calculator'),
]
```
