
""" Module for text and dataset management """

from collections import Counter
from importlib import import_module as _import
from random import randint
from .apps import INSTALLED_APPS

class DatasetManager (object):
    """ Class for managing the corpus and dataset """
    def __init__(self):
        self.__dataset = self.__get_dataset()
        self.__class_words = self.__get_classes()

        self.corpus = self.__init_corpus()

    @staticmethod
    def __get_dataset():
        dataset = {}   
        for app in INSTALLED_APPS:
            app_obj = _import(".".join(["apps", app])).App()
            dataset.update(app_obj.load_template())
        return dataset

    def __get_classes(self):
        classes = []
        for k in self.get_dataset().keys():
            classes.append (k)
        return list(set(classes))

    def __init_corpus(self):
        corpus = {}
        for c in self.__dataset.keys():
            counter = Counter(self.__dataset[c])
            corpus.update(dict(counter))
        return corpus

    # -------------------------------------------------

    def get_dataset(self):
        """Get the template data of all the installed applications to train the model """
        return self.__dataset

    def get_class_words(self):
        """ Get class names from the dataset for classification """
        return self.__class_words
