import ollama

messages = [
    {"role": "system", "content": "You are a helpful and friendly AI assistant created by Mohammed Tariq."}
]

print("\nYour local chatbot is ready! Type 'quit' to exit.\n")

while True:
    try:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("\nExiting chat...")
            break

        messages.append({"role": "user", "content": user_input})

        response = ollama.chat(
            model="mistral",  # You can replace with "llama3" or "gemma"
            messages=messages
        )

        reply = response["message"]["content"]
        messages.append({"role": "assistant", "content": reply})

        print("\nAssistant:", reply, "\n")

    except Exception as e:
        print("\nError:", e)
        print("Make sure Ollama is running and the model is installed (e.g., 'ollama pull mistral').\n")
        break
