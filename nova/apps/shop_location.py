from .base import App as BaseApp

class App (BaseApp):

    def __init__ (self):
        super().__init__()
        self.template_filename = "templates\\shop_location.json"
        self.required_entities = ["GPE"]
        self.has_asked = False
        self.locations = {
            "Yaounde": [],
            "Garoua": [],
            "Douala": [],
            "Buea": [],
            "Bamenda": [],
            "Bertoua": [],
            "Maroua": []
        }
        
    def execute (self, doc):
        # print ("app context: ", self.context)
        result = {
            "message": str(),
            "state": 0
        }
        # if the entity is a required entity by the app then add it to the context 
        for ent in doc.ents:
            if ent.label_ in self.required_entities:
                self.context[ent.label_] = ent.text
        
        # if the app has asked a question, then rather use that
        if self.has_asked != False:
            self.context["GPE"] = doc.text
        
        # if the GPE entity is given, then locate shops givn that entity, else ask for it
        if 'GPE' in self.context:
            result["message"] = "locating various LAKING Textile shops in %s" % (self.context['GPE'])
            result["state"] = 1
            self.has_asked = False
            self.context = {}
        else:
            msg  = "In which town are you looking for ?"
            for city in self.locations.keys():
                msg += "\n - %s"%(city)
            result["message"] = msg
            result["state"] = 0
            self.has_asked = True

        return result