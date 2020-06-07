""" module for conversation managing """

from .context import ContextManager


class ChatManager(object):
    """Handles the dialog/conversation"""
    def __init__(self, model_mgr, app_mgr):
        """
        Initializes a ContextManager object for handling the dialog context
        Parameters:
            model_mgr (ModelManager): instance of nova.managers.ModelManager
            app_mgr (AppManager): instance of nova.managers.AppMananager
        """
        self.model_mgr = model_mgr
        self.app_mgr = app_mgr
        self.ctx_mgr = ContextManager() # manage the chat context
        
        # self.base_classes = ["greetings", "goodbye", "ask_how", "confirm", "deny"]


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
        result = {}

        target_app = self.app_mgr.get_app_from_intent(doc._.intent)
        if target_app:
            result = target_app.execute(doc)
            if result["state"] == 0:
                self.ctx_mgr.set_context(doc._.intent)
            else:
                self.ctx_mgr.reset_context()
        # if no intent matches, then he probably dont understand
        else:
            result["message"] = "sorry I do not understand what you mean"
        # return the message from the executed app
        return result['message']

    # -----------------------------------------------

    def respond(self, msg):
        """
        Gives a response to a given message
        Parameters:
            msg(str): the message to which is reponse is to be given
        Returns a str object
        """
        return self.__respond(msg)