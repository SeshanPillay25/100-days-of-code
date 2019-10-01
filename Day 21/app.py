#Basic implementation  of a vending machine chatbot in python
import random
# from speech import *
from pip._vendor.distlib.compat import raw_input

CONVERSING = True

memory = []
greetings = ['hola', 'hello', 'hi', 'hey!', 'Hello', 'Hi']
questions = ['How are you?', 'How are you doing?']
responses = ['Okay', 'I am fine']
validations = ['yes', 'yeah', 'yea', 'no', 'No', 'Nah', 'nah']
items = ['Fruit/Sweets', 'Chocolates/Drinks ', 'Nuts']
verifications = ['Are you sure?', 'You sure?', 'you sure?', 'sure?', "Sure?"]

engagement_pairs = (greetings, greetings), (questions, responses), (verifications, validations)

while CONVERSING:
    lang = 'en-US'
    speed = .3

    userInput = raw_input(">>>Me: ")
    for triggers, outputs in engagement_pairs:
        if not userInput in triggers:
            continue

        random_output = random.choice(outputs)

        # say(random_output, lang, speed)
        print(random_output)
        memory.append((userInput, random_output))
        break

    else:
        if 'sure' in userInput:
            response = "Sure about what?"
            # say(response,lang,speed)
            memory.append(('sure', response))
            print(response)
        else:
            CONVERSING = False