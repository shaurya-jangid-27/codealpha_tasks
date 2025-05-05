import nltk
import random
from nltk.chat.util import Chat, reflections

# Some basic conversation pairs
pairs = [
    [
        r"hi|hello|hey",
        ["Hello there!", "Hi!", "Hey! How can I help you today?"]
    ],
    [
        r"what is your name ?",
        ["I am your personal chatbot."]
    ],
    [
        r"how are you ?",
        ["I'm just a bunch of code, but thanks for asking!", "I'm doing great! What about you?"]
    ],
    [
        r"sorry",
        ["No problem at all!", "It's okay, no worries."]
    ],
    [
        r"I am fine|I am good|I'm good",
        ["That's great to hear!", "Awesome, how can I assist you today?"]
    ],
    [
        r"what can you do ?",
        ["I can chat with you and help you learn Python basics! Try asking me about Python, variables, or functions."]
    ],
    [
        r"quit|bye|exit",
        ["Goodbye! Have a nice day ", "See you soon!", "Exiting chat..."]
    ],
    [
        r"(.*)",
        ["I can't understand what you're talking about."]
    ]
]

def chatbot():
    print(" Hello! I am your chatbot. Type 'quit' to exit.")
    print(" I can talk to you in English. Let's chat!")
    chat = Chat(pairs, reflections)
    chat.converse()

if name == "main":
    nltk.download('punkt')  # Only needed once
    chatbot()