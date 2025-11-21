def chatbot():
    print("Chatbot ready! Type 'bye' to exit.")
    while True:
        user = input("You: ").lower()
        if user in ["hello", "hi"]:
            print("Bot: Hi!")
        elif user in ["how are you"]:
            print("Bot: I'm fine, thanks!")
        elif user in ["bye", "exit"]:
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand.")

chatbot()