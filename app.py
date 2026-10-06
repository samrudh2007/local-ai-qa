from ollama import chat

while True:
    question = input("You: ")

    if question == "exit":
        print("AI: Goodbye!")
        break

    response = chat(
        model="gemma3:1b",
        messages=[
            {
                "role": "system",
                "content": "You are a concise AI assistant. Answer clearly and briefly."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    print("AI:", response.message.content)