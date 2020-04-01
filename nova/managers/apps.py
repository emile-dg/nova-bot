"""Module for apps management"""

from importlib import import_module


INSTALLED_APPS = ["base"]
bot_context = str()

class AppManager(object):
    """The AppManager is ment to manipulate NOVA apps/fetaures"""
    def __init__(self):
        self.installed_apps = INSTALLED_APPS
        self.dispatched_apps = self.__app_dispatcher()

    def __app_dispatcher(self):
        """gets and returns a dictionary of installed apps as keys and the application's 'App()' instance as value"""
        _temp = {}
        for app in self.installed_apps:
            _temp.update ({app: import_module(".".join(["apps",app])).App()})
        return _temp