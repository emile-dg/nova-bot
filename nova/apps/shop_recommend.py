from .base import App as BaseApp

class App (BaseApp):

    def __init__ (self):
        super().__init__()
        self.template_filename = "templates\\shop_recommend.json"
        self.possible_purposes = [
            "marriage", "funeral", "school", "other", "ceremony"
        ]
        
    def execute (self, doc):
        result = { "message": "Recommending",  "state": 1 }


        for token in doc:
            if token.dep_ != "-" and token.dep_ != "ACTION":
                self.context[token.dep_] = token.text
        
        # print (self.context)

        return result
        # print ("Recommend: ")
        # for t in doc:
        #     if t.dep_ != "-":
        #         print ("  |", t, " : ", t.dep_)