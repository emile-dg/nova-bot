from os import system
from sys import argv

import spacy

from managers.models import ModelManager
from managers.apps import AppManager, INSTALLED_APPS
from managers.chat import ChatManager

# from trainer import train_model


if __name__ == "__main__":
    model_mgr = ModelManager("model", create_on_404=True)
    print("- Model loaded!")

    app_mgr = AppManager()
    print("- Apps ready!")

    chat_mgr = ChatManager(model_mgr, app_mgr)
    print("- Chat ready!")

    # if "train-bot" in argv:
    #     print("- Training...")
    #     train_model(model_mgr)
    #     print("- BECCA trained!")

    system("pause")
    system("cls")
    print("\n - Hello, I'm BECCA, \n - How then can I help you ? :)")

    while True:
        try:
            user_msg = input(">>> ")
            print(chat_mgr.respond(user_msg))
        except KeyboardInterrupt:
            break
