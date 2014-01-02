from django.conf import settings
try:
    from django.utils.module_loading import import_by_path
except ImportError:
    from django.utils.importlib import import_module
    from django.core.exceptions import ImproperlyConfigured

    def import_by_path(dotted_path):
        try:
            module_path, class_name = dotted_path.rsplit('.', 1)
            module = import_module(module_path)
            return getattr(module, class_name)
        except AttributeError:
            raise ImproperlyConfigured(
                'Module "%s" does not define a "%s"' % (module_path,
                                                        class_name))
        except ImportError:
            raise ImproperlyConfigured(
                "No such module '%s'" % module_path)


def setting(name, default=None):
    """
    Helper function to get a Django setting by name or (optionally) return
    a default (or else ``None``).
    """
    return getattr(settings, name, default)
