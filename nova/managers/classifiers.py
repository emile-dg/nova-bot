
""" Module for text classification """


import nltk
from nltk.stem.lancaster import LancasterStemmer

from .text import DatasetManager

dataset__man = DatasetManager()
corpus = dataset__man.corpus
class_words = dataset__man.get_dataset()

stemmer = LancasterStemmer()

class IntentClassifier (object):
    name = "intent_classifier"

    def __init__ (self, nlp, **arg):
        self.nlp = nlp

    def calculate_class_score(self, sentence, class_name, show_details=True):
        score = 0
        for word in nltk.word_tokenize(sentence):
            if stemmer.stem(word.lower()) in class_words[class_name]:
                score += (1 / corpus[stemmer.stem(word.lower())])
                if show_details:
                    print ("   match: %s (%s)" % (stemmer.stem(word.lower()), 1 / corpus[stemmer.stem(word.lower())]))
        return score

    def __call__ (self, doc):
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
        # if high_score > 1:
        doc._.intent = high_class

        return doc