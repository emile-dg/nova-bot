""" module for conversation managing """

from .context import ContextManager


class ChatManager(object):
    def __init__(self, model_mgr, app_mgr):
        self.model_mgr = model_mgr
        self.app_mgr = app_mgr
        self.ctx_mgr = ContextManager() # manage the chat context
        
        self.base_classes = ["greetings", "goodbye", "ask_how", "confirm", "deny"]


    def __respond(self, msg):
        return self.__dispatcher(self.model_mgr.model(str(msg)))

    def __result_from_app(self, doc):
        pass

    def __dispatcher(self, doc):
        # print ("dispatcher context [before]: ", self.ctx_mgr.get_context(), doc._.intent)
        temp = None
        result = {}

        if self.ctx_mgr.has_context():
            doc._.intent = self.ctx_mgr.get_context()
            temp = self.ctx_mgr.get_context()
            self.ctx_mgr.reset_context() 
        else:
            self.ctx_mgr.set_context(doc._.intent)

        # dispatch the doc to the appropriate app based on the intent
        if doc._.intent in self.app_mgr.dispatched_apps:
            result = self.app_mgr.dispatched_apps[doc._.intent].execute(doc)
            if result["state"] == 0:
                self.ctx_mgr.set_context(doc._.intent)
            else:
                self.ctx_mgr.reset_context()

        elif doc._.intent in self.base_classes:
            result = self.app_mgr.dispatched_apps["base"].execute (doc)
            self.ctx_mgr.reset_context()

        else :
            if temp:
                result = self.app_mgr.dispatched_apps[doc._.intent].execute(doc)
                if result["state"] == 0:
                    self.ctx_mgr.set_context(doc._.intent)
                else:
                    self.ctx_mgr.reset_context()
            else:
                result["message"] = "sorry I didn't get what you said!"

        # print ("dispatcher context [after]: ", self.ctx_mgr.get_context(), doc._.intent)
        return result['message']

    # -----------------------------------------------

    def respond(self, msg):
        """ method for getting the bot response to a given message """
        return self.__respond(msg)