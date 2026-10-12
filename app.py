from ollama import chat

with open("notes.txt", "r") as file:
    document = file.read()

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
        "content": "Answer using the provided document. If the answer is not in the document, say you don't know."
    },
    {
        "role": "user",
        "content": f"Document:\n{document}\n\nQuestion:\n{question}"
    }
]
    )

    print("AI:", response.message.content)