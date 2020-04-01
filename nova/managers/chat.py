""" module for conversation managing """

from .context import ContextManager


class ChatManager(object):
    """Handles the dialog/conversation"""
    def __init__(self, model_mgr, app_mgr):
        """
        Initializes a ContextManager object for handling the dialog context
        Parameters:
            model_mgr (ModelManager): instance defined as model manager for the chatbot
            app_mgr (AppManager): instance defined as app manager for the chatbot
        """
        self.model_mgr = model_mgr
        self.app_mgr = app_mgr
        self.ctx_mgr = ContextManager() # manage the chat context
        
        self.base_classes = ["greetings", "goodbye", "ask_how", "confirm", "deny"]


    def __respond(self, msg):
        """Gives a response to a given message"""
        return self.__dispatcher(self.model_mgr.model(str(msg)))

    def __result_from_app(self, doc):
        pass

    def __dispatcher(self, doc):
        """
        Dispatch the doc object to the appropriate app 
        based on the intent and context of the chat
        Parameter:
            doc (spacy.Doc): spacy doc object
        Returns a str obtained from the dispatched app
        """
        temp = None
        result = {}

        # if a context exists in the context manager, 
        # then set it as intent to redirect the message
        # to the previous application, use that intent 
        # then reset the context manager
        if self.ctx_mgr.has_context():
            doc._.intent = self.ctx_mgr.get_context()
            temp = self.ctx_mgr.get_context()
            self.ctx_mgr.reset_context() 
        # else add the actual intent to the context manager
        else:
            self.ctx_mgr.set_context(doc._.intent)

        # dispatch the doc to the appropriate app based on the intent
        if doc._.intent in self.app_mgr.dispatched_apps:
            # store the response from the App.execute() method passing 
            # the doc as argument. result is always a dictionary
            result = self.app_mgr.dispatched_apps[doc._.intent].execute(doc)
            # state means the condition under which the app is left after
            # giving a response. It is used to ask the chat manager to set 
            # the context to itself after returning mostly a question and 
            # is awaiting for a response.
            #   state is 0 when the app awaits for the next message and 
            #   state 1 means that the apps is done and the context is then reset
            if result["state"] == 0:
                self.ctx_mgr.set_context(doc._.intent)
            else:
                self.ctx_mgr.reset_context()

        # if the intent belongs to the base classes, then dispatch the 
        # doc to the base App and reset the context manager
        elif doc._.intent in self.base_classes:
            result = self.app_mgr.dispatched_apps["base"].execute(doc)
            self.ctx_mgr.reset_context()
        # if not dispatch to the approriate App, if necessary, add to context 
        # or remove from context
        else :
            if temp:
                result = self.app_mgr.dispatched_apps[doc._.intent].execute(doc)
                if result["state"] == 0:
                    self.ctx_mgr.set_context(doc._.intent)
                else:
                    self.ctx_mgr.reset_context()
            # if he doesnot understand what is said
            else:
                result["message"] = "sorry I didn't get what you said!"

        # return the message from the executed app
        return result['message']

    # -----------------------------------------------

    def respond(self, msg):
        """
        Gives a response to a given message
        Parameters:
            msg(str): the message to which is reponse is to be given
        Returns a str
        """
        return self.__respond(msg)