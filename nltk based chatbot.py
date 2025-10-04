import nltk
import random
import string

# Download NLTK resources (only the first time you run it)
nltk.download("punkt")
nltk.download("wordnet")

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# --- Expanded intents ---
intents = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "goodbye", "see you later", "farewell", "catch you later"],
    "thanks": ["thanks", "thank you", "appreciate it"],
    "age": ["how old are you", "what is your age"],
    "name": ["what is your name", "who are you", "tell me about yourself"],
    "feeling": ["how are you", "how's it going", "how do you feel"],
    "default": ["I’m not sure I understand. Could you rephrase that?"]
}

# --- More natural responses ---
responses = {
    "greeting": ["Hey there!", "Hi, good to see you!", "Hello! How’s your day going?"],
    "goodbye": ["Goodbye! Take care.", "See you soon!", "Bye! Have a great day."],
    "thanks": ["No worries.", "Anytime.", "Happy to help."],
    "age": ["I don’t really have an age… I live in your computer."],
    "name": ["I’m a simple chatbot coded by Mohammed Tariq.", "People call me TariqBot."],
    "feeling": ["I’m doing great, thanks for asking! How about you?", "I feel like chatting today!"],
    "default": ["Hmm, I’m not sure I got that. Could you say it another way?"]
}

# --- Preprocessing ---
def preprocess(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return tokens

# --- Intent Classification ---
def classify(sentence):
    tokens = preprocess(sentence)
    for intent, examples in intents.items():
        for example in examples:
            if all(word in tokens for word in example.split()):
                return intent
    return "default"

# --- Chat loop ---
print("\nSimple NLP Chatbot (type 'quit' to exit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye!")
        break

    intent = classify(user_input)
    reply = random.choice(responses[intent])
    print("Chatbot:", reply)
