import json

import nltk
from nltk import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
from string import punctuation
from datetime import datetime
from random import choice

stemmer = LancasterStemmer()

class App:
    """Base app"""
    def __init__(self):
        self.template_filename = "templates\\base.json"
        self.__context = {}
        self.__responses = self.__load_responses()
        self.intents = self.__load_intents()

    def __load_intents(self):
        """Get a tuple of all intents from the app template"""
        return tuple(set(self.load_template().keys()))
        
    def load_template(self):
        r"""
        returns a dictionary of the format:
            {
                "intent 1": ["intent 1", "intent 2"],
                "intent 2": []
            }
        """
        raw = {}
        try:
            with open (self.template_filename, "r") as file:
                intents = json.load(file)["intents"]
                for intent in intents:
                    class_name = intent['name']
                    raw[class_name] = []
                    for sentence in intent['sentences']:
                        for word in word_tokenize(sentence[0]):
                            if word not in punctuation:
                                raw[class_name].append (stemmer.stem(word.lower()))
        except Exception:
            raise Exception("An error occured while trying to load template file: ", self.template_filename)

        finally:
            return raw

    @staticmethod
    def get_moment():
        """
        Used to generate appropriate greeting. Returns 'morning', 'afternoon' 
        or 'evening', based on the actual computer system time
        """
        hour = datetime.now().hour
        if hour >= 5 and hour <= 12:
            return "morning"
        elif hour > 12 and hour <= 18:
            return "afternoon"
        else:
            return "evening"

    def __load_responses(self):
        """Load the responses from the template"""
        responses = []
        try:
            with open (self.template_filename, "r") as file:
                for resp in json.load (file)["responses"]:
                    responses.append ( { resp["type"]: resp["answers"] })
        except Exception as e: 
            print ("An error occured while trying to load responses from file [", self.template_filename, "]\n\t", e)
        finally:
            return responses

    def execute(self, doc):
        """Returns a dict with a response to the given message
        and a state to mean if the response is a question asking 
        for something or not"""
        intent = doc._.intent
        moment = self.get_moment()
        r = str()
        for resp in self.__responses:
            if intent in resp:
                r = choice(resp[intent])
                break
        print ("[debug] intent: ", intent)
        if intent == "greetings":
            return {
                "message": r.format(m=moment),
                "state": 1
            }
        else:
            return {
                "message": r,
                "state": 1
            }   

    def has_intent(self, intent):
        return intent in self.intents