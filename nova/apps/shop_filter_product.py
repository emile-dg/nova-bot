from .base import App as BaseApp

class App (BaseApp):

    def __init__ (self):
        super().__init__()
        self.template_filename = "templates\\shop_filter_product.json"
        
    def execute (self, doc):
        result = {
            "message": "Filter: Ok, let me check what I can get for you", 
            "state": 1
        }
        return result
        # print ("Filter: ")
        # for t in doc:
        #     if t.dep_ != "-":
        #         print ("  |", t, " : ", t.dep_)