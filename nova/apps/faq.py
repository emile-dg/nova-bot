from apps.base import App as BaseApp
from random import choice

class App(BaseApp):
    """FAQ"""
    def __init__(self):
        self.template_filename = "templates\\faq.json"
        self.__context = {}
        self.__responses = self.__load_responses()
        self.intents = self.__load_intents()

    def execute(self, doc):
        """::overwrites apps.base.App.execute method"""
        intent = doc._.intent
        for resp in self.__responses:
            if intent in resp:
                r = choice(resp[intent])
                break
        print ("[debug] intent: ", intent)
        return {
            "message": r,
            "state": 1
        } 