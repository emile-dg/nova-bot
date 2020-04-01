""" Module for text classification """

import nltk
from nltk.stem.lancaster import LancasterStemmer

from .text import DatasetManager

# instanciate the Dataset manager,
# get the corpus and the classes
dataset_man = DatasetManager()
corpus = dataset_man.corpus
class_words = dataset_man.get_dataset()
# use LancasterStemmer as stemmer
stemmer = LancasterStemmer()

class IntentClassifier (object):
    """Implements various text classification algorithms to determine the intent"""

    name = "intent_classifier"
    def __init__ (self, nlp, **arg):
        """
        Paramters:
            nlp (spacy): the natural language processor from the ModelManager.model
        """
        self.nlp = nlp

    def calculate_class_score(self, sentence, class_name, show_details=True):
        """
        Implements the Naive Bayes algorithm to classify a text
        Parameters:
            sentence (str): the text to classify
            class_name (tuple): a list of classes
            show_details (bool) : print the match for debugging purposes
        Returns float
        """
        score = 0
        for word in nltk.word_tokenize(sentence):
            if stemmer.stem(word.lower()) in class_words[class_name]:
                score += (1 / corpus[stemmer.stem(word.lower())])
                if show_details:
                    print ("   match: %s (%s)" % (stemmer.stem(word.lower()), 1 / corpus[stemmer.stem(word.lower())]))
        return score

    # automatically called as part of the pipleine when processing the doc
    def __call__ (self, doc):
        """Returns the doc after classifying it's text intent"""
        high_class = None
        high_score = 0
        # loop through our classes
        for c in class_words.keys():
            # calculate score of doc for each class
            score = self.calculate_class_score(doc.text, c, show_details=False)
            # keep track of highest score
            if score > high_score:
                high_class = c
                high_score = score
        # set the intent then return the doc back
        doc._.intent = high_class
        return doc