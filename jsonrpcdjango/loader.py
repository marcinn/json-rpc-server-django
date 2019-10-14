
def load_service_instance(path):
    try:
        from django.utils.importlib import import_module
    except:
        from importlib import import_module

    from django.core.exceptions import ImproperlyConfigured
    i = path.rfind('.')
    module, attr = path[:i], path[i+1:]
    try:
        mod = import_module(module)
    except ImportError as e:
        raise ImproperlyConfigured('Error importing JSON-RPC service instance %s: "%s"' % (path, e))
    except ValueError as e:
        raise ImproperlyConfigured('Error importing JSON-RPC instance: %s' % e)
    try:
        obj = getattr(mod, attr)
    except AttributeError:
        raise ImproperlyConfigured('Module "%s" does not define a "%s" JSON-RPC instance' % (module, attr))
    return obj


