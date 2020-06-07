"""Module for apps management"""

from importlib import import_module


INSTALLED_APPS = [
    "base", 
    "shop_locate",
    "faq",
]
bot_context = str()

class AppManager(object):
    """The AppManager is ment to manipulate NOVA apps/fetaures
    \n[WARNING]: Avoid declaring more than one instance
    """
    def __init__(self):
        self.installed_apps = INSTALLED_APPS
        self.dispatched_apps = self.__app_dispatcher()

    def __app_dispatcher(self):
        """gets and returns a dictionary of 
        installed apps as keys and the application's 
        'App()' instance as value
        """
        _temp = {}
        for app in self.installed_apps:
            try:
                _temp.update ({app: import_module(".".join(["apps",app])).App()})
            except ImportError:
                raise ImportError(f"Error, app '{app}' not found")
            except:
                raise Exception("Error, an unexpected error occured while loading installed apps")
        return _temp

    def get_app_from_intent(self, intent):
        for app in self.dispatched_apps.keys():
            if self.dispatched_apps[app].has_intent(intent):
                return self.dispatched_apps[app]
        return None