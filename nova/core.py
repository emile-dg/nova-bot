from os import system
from sys import argv

import spacy

from managers.models import ModelManager
from managers.apps import AppManager
from managers.chat import ChatManager

from trainer import train_model


if __name__ == "__main__":
    # get the model and create a new one if not founc
    model_mgr = ModelManager("model", create_on_404=True)
    print("- Model loaded!")

    app_mgr = AppManager()
    print("- Apps ready!")

    chat_mgr = ChatManager(model_mgr, app_mgr)
    print("- Chat ready!")

    if "train-bot" in argv:
        # print("- Training...")
        train_model(model_mgr)
        # print("- NOVA trained!")

    while True:
        try:
            user_msg = input(">>> ")
            print(chat_mgr.respond(user_msg))
        except KeyboardInterrupt:
            break
