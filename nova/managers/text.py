""" Module for text and dataset management """

from collections import Counter
from importlib import import_module as _import
from random import randint
from .apps import INSTALLED_APPS

class DatasetManager (object):
    """Class for managing the corpus and dataset"""
    def __init__(self):
        """Initialize the dataset and known word classes"""
        self.__dataset = self.__get_dataset()
        self.__class_words = self.__get_classes()
        self.corpus = self.__init_corpus()

    @staticmethod
    def __get_dataset():
        """
        Loads all templates' intents and words from installed applications
        returns a dictionary with the same format as that of the 
        App load_template method but rather for all installed apps.
        """
        dataset = {}   
        # get the templates' data for all installed 
        # application and update to the dataset
        for app in INSTALLED_APPS:
            # make a instance of the app App then update
            # the dataset with the result from the instance's
            # laod_template method
            app_obj = _import(".".join(["apps", app])).App()
            dataset.update(app_obj.load_template())
        return dataset

    def __get_classes(self):
        """get and returns a list of all unique intents(classes)"""
        return list(set([k for k in self.__dataset.keys()]))

    def __init_corpus(self):
        """
        get and returns the corpus; a dictionary of all
        known words with their frequency in the dataset.
        returns corpus(dict).
        """
        corpus = {}
        for c in self.__dataset.keys():
            counter = Counter(self.__dataset[c])
            corpus.update(dict(counter))
        return corpus

    # -------------------------------------------------

    def get_dataset(self):
        """returns dictionary: the dataset"""
        return self.__dataset

    def get_class_words(self):
        """returns list: known class names"""
        return self.__class_words
