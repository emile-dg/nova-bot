
""" This module provides basic management of models of the NLP engine """


from pathlib import Path

import spacy
from spacy.language import Language
from spacy.tokens import Doc

from .classifiers import IntentClassifier


class ModelManager(object):
    def __init__(self, model_path, create_on_404=False, default_model="en_core_web_sm"):
        self.model_path = model_path

        Language.factories['intent_classifier'] = lambda model, **cfg: IntentClassifier(model, **cfg)
        
        if self.__model_exists ():
            self.model = spacy.load (self.model_path)
        else:
            # if asked to cerate a new model in case the model does not exist
            if create_on_404: 
                self.model = spacy.load (default_model)
            else:
                raise ModuleNotFoundError("The NLP model not found!")

        
        Doc.set_extension("intent", default=None, force=True)
        if "intent_classifier" not in self.model.pipe_names:
            self.model.add_pipe(IntentClassifier)

    def __model_exists(self, dir_name=None):
        # check if the directory name exists then return the result
        if dir_name != None: 
            path = Path(dir_name)
        else:
            path = Path(self.model_path)
        if path.exists():
            return True
        else:
            return False

    def save_model(self):
        """Save the model"""
        self.model.to_disk (self.model_path)
