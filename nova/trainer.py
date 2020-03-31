
""" Module for training the bot """

import json
from random import shuffle as random_shuffle

from spacy.util import compounding, minibatch


def create_parser (nlp):
    """"Setup and return the parser"""
    # use build-in dependency parser class using a new instance
    if "parser" in nlp.pipe_names:
        nlp.remove_pipe ("parser")
    parser = nlp.create_pipe("parser")
    nlp.add_pipe(parser, last=True)
    return parser

def train_model_dep (nlp, dataset, parser, n_iter=15):
    """Train a given model on a given dataset for n_iter times"""
    # get the labels
    for _, annotation in dataset:
        for dep in annotation.get("deps", []):
            parser.add_label(dep)
    pipe_exceptions = ["parser", "trf_wordpiecer", "trf_tok2vec", "intent_classifier"]
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions] # to be ignored
    # train only the parser
    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.begin_training()
        for _ in range(n_iter):
            random_shuffle(dataset)
            losses = {}
            batches = minibatch(dataset, size=compounding(4.0, 32.0, 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, losses=losses)
    return losses

def train_model (model_man):
    """
    Train the model
    """
    print ("- Training the bot...")
    nlp = model_man.model
    model_man.save_model()

    reg_dataset = []
    parser = create_parser(nlp)

    # # load the templates for all installed apps then append to the dataset
    with open ("templates\\entity_reg_trainer.json", "r") as file:
        template = json.load(file)

    # get the dep and doc from the template
    for t, dep in template['templates']:
        nlp.begin_training()
        doc = nlp(t)
        reg_dataset.append((t, {"heads":[token.head.i for token in doc], "deps":dep})) # addings heads
    
    train_model_dep(nlp, reg_dataset, parser)
    print ("- Training finish!")
    model_man.save_model()
    print ("- Model saved!")
