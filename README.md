NOVA Bots
=========

Introduction
-----------
Nova bots is an easy-to-use python framework for developing multilingual AI-based chatbots 
for businesses or simple conversations. Nova can be used to make automated and intelligent dialogue 
systems like customer support, personal assistance, commercial agents, and more. It is developed with 
the modularity of features in mind (i.e. every functionality of the bot is considered an 'app' and can 
be plugged and removed easily from the system without affecting the Bot itself. This makes the bot 
reusable) and easy to train.


INSTALLATION GUIDE
------------------
To setup and make the project ready to use, you simply need to download the repo, decompress it,
install all the required libraries in the `requirements.txt` file in the project repo. To do so, 
=======
install all the required libraries in the *requirements.txt* file in the project repo. To do so,
simply type in the following command using the command prompt on windows.
*N.B*: A prior basic knowledge of using the command prompt is needed. This assumes that python have
beed installed and pip added to the `ENVIRONMENTAL PATH VARIABLE`. If not, download python from
[Here](http://www.python.org). Make sure to use python 3.6 or higher. If possible use `virtual 
environments` to isolate the project.
```shell
    pip install -r requirements.txt
```
When the installation is over, you can now run the project by following steps below:
```shell
    cd nova
    python core.py
```
The program should then execute and you could chat with the bot. The Bot basic features are:
- Basic greetings
This means that Nova can reply to simple greetings like 'good morning', 'how are you?'
and 'goodbye'. You will learn how to extend the features further in this guide.

How to extend Nova with new features
------------------------------------
### 1. Creating the feature / application
NB: The terms Feature and Application can be use interchangeably 
1. Create an new python module in the apps package and give it a name. 
Let's call it ``new_feature.py``. Follow the python convention of naming
modules
2. Open the newly created module and type in the following python script.
I'll explain the code below
```python
    from apps.base import App as BaseApp

    class App(BaseApp):
        """Always add a docstring"""
        def __init__(self):
            self.template_filename = "templates\\new_feature.json"
            self.__context = {}
            self.__responses = self.__load_responses()

        def execute(self, doc):
            """::overwrites apps.base.App.execute method"""
            print("new feature")
```
- Fist we import the ``App`` class from the ``base`` module in the ``apps`` package
as ``BaseApp`` to act as the base application or parent of our new
application. This is optional but recommended for beginners, avoid only if you 
know what you are doing. 
- Now we create a new class called ``App`` (always) and make it inherits 
from the ``BaseApp``. Don't forget to add a doctring ;)
- In the ``__init__`` method, we overwrite the ``BaseApp`` initial variables 
    - ``self.template_filename`` refers to the file containing the templates
    for training our intent clasifier. This is required
    - We'll look at the 2 others further in this guide
- The ``execute`` method should always exist to overwrite the ``BaseApp.execute`` method. We'll come to it in a moment.

### 2. Adding templates for training
To train Nova to recognize new intents for our newly created feature, we need to 
create a ``json`` file in the ``templates`` folder of the project and give a name.
It is recommended to call it with the feature name. In our case, 
``new_feature.json``. The structure of the file is as follows:
```json
    {
        "intents": [
            {
                "name": "new_feature",
                "sentences": [
                    "sample text",
                    "another sample text"
                ]
            }
        ]
    }
```
NB: You can add more than a single intent but for now, let's add just one.
But always make sure to always give a unique name to you intent. If your apps
intent may conflict, use the app name, followed by an underscore and then the 
intent. Example: `restaurant_search` to mean a search intent for a feature 
called `restaurant`.

### 3. Installing the new feature/application
If all of the above steps have been followed, then we can now make sure Nova
knows that we've added a new feature to it. 
- First open the ``apps.py`` module in the ``managers`` package. 
- Now you'll see a list called ``INSTALLED_APPS``. It should look like 
```python
    INSTALLED_APPS = ["base"]
```
This means that only the ``apps.base`` app in installed. Let's add our new 
application by simply adding the app name. write the exact name of the 
module in the ``apps`` package.
```python
    INSTALLED_APPS = ["base", "new_feature"]
```
- Hourah!!, our application have been installed successfully. Now let's train Nova
by running the following command in you shell
```shell
    python core.py train-bot
```
The ``train-bot`` argument tells nova to train the model.
- Now we are done with this section of the guide. Now that Nova is running, 
try to type one of the sentences you've given in the new_feature template 
json file and you should see the following output:
```shell
    >>> sample text
    new feature
```
In the next tutorial we shall see how to implement a complete application
and we will implement the application ``execute`` method and dive deeper
into the topic.


Quickstart and Usage
--------------------



Project TODO
------------
- [x] Add smalltalk as base app
- [x] Add shop_localize application
- [ ] Add shop_recommend application
- [ ] Add shop_order application



CHANGELOG
---------
