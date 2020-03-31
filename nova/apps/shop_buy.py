from .base import App as BaseApp

class App (BaseApp):

    def __init__ (self):
        super().__init__()
        self.template_filename = "templates\\shop_buy.json"

    def execute (self, doc):
        result = {
            "message": "Order: Ok, let me register your order...",
            "state": 1
        }
        return result