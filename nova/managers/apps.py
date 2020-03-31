
""" Module for apps managements """

from importlib import import_module


INSTALLED_APPS = ["base"]
bot_context = str()

class AppManager(object):
    """ The app manager """
    def __init__(self):
        self.installed_apps = INSTALLED_APPS
        self.dispatched_apps = self.__app_dispatcher()

    def __app_dispatcher(self):
        _temp = {}
        for app in self.installed_apps:
            _temp.update ({app: import_module(".".join(["apps",app])).App()})
        return _temp