from django.core.exceptions import ImproperlyConfigured
from jsonrpcdjango.loader import load_service_instance
import pytest


def test_load_service_instance():
    # Test loading a valid object
    obj = load_service_instance('jsonrpcdjango.loader.load_service_instance')
    assert obj is load_service_instance

    # Test loading from a non-existent module
    with pytest.raises(ImproperlyConfigured):
        load_service_instance('non_existent_module.some_object')

    # Test loading a non-existent object from a valid module
    with pytest.raises(ImproperlyConfigured):
        load_service_instance('jsonrpcdjango.loader.non_existent_object')
