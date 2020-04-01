""" This module provides basic management of models of the NLP engine """

from pathlib import Path

import spacy
from spacy.language import Language
from spacy.tokens import Doc

from .classifiers import IntentClassifier


class ModelManager(object):
    """Manipulate the NLP engine and models"""
    def __init__(self, model_path, create_on_404=False, default_model="en_core_web_sm"):
        """
        Initialzes the model
        Parameters:
            model_path (str): the path to the model
            --optional
            create_on_404 (bool): wether to create a new model in case the model wasn't found. Default is False
            default_model (str): the default model to use in case a new model is created. Default is 'en_core_web-sm'. Refer to spacy models for this
        If the model was not found and create_on_404 is False, it will raise a ModuleNotFoundError.
        If the default_model is overwritten, a possible exception in case the model wan't found by spacy is not handled.
        """
        self.model_path = model_path
        # add the IntentClassifier to language factories
        Language.factories['intent_classifier'] = lambda model, **cfg: IntentClassifier(model, **cfg)
        
        if self.__model_exists ():
            self.model = spacy.load(self.model_path)
        else:
            if create_on_404: 
                self.model = spacy.load(default_model)
            else:
                raise ModuleNotFoundError("The NLP model not found!")
        # add the intent attribute to the doc
        Doc.set_extension("intent", default=None, force=True)
        # add the intent classifier to the pipeline if not present
        if "intent_classifier" not in self.model.pipe_names:
            self.model.add_pipe(IntentClassifier)

    def __model_exists(self, dir_name=None):
        """
        check if the directory name exists then return the result
        by defaults check for the actual model. 
        Parameters:
            dir_name (str): path to the model to check. Its optional and default is None
        Returns bool
        """
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
