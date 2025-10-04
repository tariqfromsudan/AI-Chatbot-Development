# AI Chatbots (Ollama + NLTK)

## 📌 Overview
This repository contains two chatbot implementations built with Python, showcasing different approaches to conversational AI.  
The **Ollama-based chatbot** connects with local large language models (LLMs) such as Mistral or LLaMA 3 for natural, flexible responses.  
The **NLTK-based chatbot** is a lightweight rule-based system that uses tokenization and intent recognition to simulate conversation.  
Together, they demonstrate both modern AI-driven and classic NLP-driven chatbot design.  

---

## 🚀 Features

- **Ollama Chatbot (`chatbot.py`)**
  - Powered by local large language models (Mistral, LLaMA, Gemma).  
  - Generates natural, context-aware responses.  
  - System role definition + conversation history.  
  - Error handling if Ollama is not running or models aren’t installed.  

- **NLTK Chatbot (`nltk_chatbot.py`)**
  - Rule-based chatbot using Natural Language Toolkit (NLTK).  
  - Handles greetings, FAQs, and fallback responses.  
  - Uses tokenization and lemmatization for simple intent recognition.  
  - Lightweight and easy to extend.  

---

## 📦 Requirements

- Python 3.9+  
- Dependencies (install with pip):  
  ```bash
  pip install -r requirements.txt

---

## 🧑‍💻 How to Run

### Running the Ollama Chatbot

1. Make sure [Ollama](https://ollama.ai) is installed and running.
2. Pull a model (e.g. Mistral):

   ```bash
   ollama pull mistral
   ```
3. Run the chatbot:

   ```bash
   python chatbot.py
   ```

### Running the NLTK Chatbot

1. Run the script:

   ```bash
   python nltk_chatbot.py
   ```
2. The first time, it will download required NLTK data (punkt, wordnet).
3. Chat in the terminal with greetings, FAQs, or test fallback responses.

---

## 📂 Project Structure

```
AI-Chatbot-Development/
├── olama based chatbot.py             
├── nltk based chatbot.py    
├── REPORT.pdf               
├── requirements.txt          
└── README.md           
```

---

## 📑 Notes

* Default Ollama model is set to `mistral`. You can change it in `chatbot.py`.
* Both chatbots run locally, with no external API costs.
* Designed as a **learning project** to explore LLM integration and NLP fundamentals side by side.

```
