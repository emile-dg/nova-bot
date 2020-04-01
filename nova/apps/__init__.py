r"""
Package of apps or bot features.
...An app is a python module representing what the bot can do. It is used when a given
user message intent matches the app intent. Then the App execute method is called 
passing the doc oject as argument. 
...The App inherits from base.App class to extend and override some of the base class 
methods. Refer to the base module for more information. The inheritance is optional
but recommended to avoid reimplementing basic stuffs like loading the template and responses.

Quickstart
----------
Follow the steps below to create an app or feature
    1. inside the the apps package, create a python script and name it the way you want (avoid using 'app.py' itself)
    2. use the below app nomencleture:
        ```python
            from .base app import App as BaseApp

            class App(BaseApp):
                def __init__(self):
                    self.template_filename = "templates\\my_template.json"
                    super().__init__()
                
                def execute(self, doc):
                    # process the doc at your will then return a dict
                    # having the response message and the actual state
                    # of the app
                    return {
                        "message": "your response",
                        "state: 1
                    }
                
                def custom_method(self, param):
                    # do something
                    return 
        ```
    ...For more detailed information about the creation and usage of apps, refer to the documentation in the project 
    ...docs folder.
"""