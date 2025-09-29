def chatbot():
    print("Chatbot: Hi! Type 'quit' to exit.")
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == 'quit':
            print("Chatbot: Bye!")
            break
        elif user_input in ['hello', 'hi']:
            print("Chatbot: Hi there!")
        elif user_input == 'how are you':
            print("Chatbot: I'm doing great, thanks!")
        elif user_input == 'what is your name':
            print("Chatbot: I'm a simple bot!")
        else:
            print("Chatbot: Sorry, I didn't get that.")
chatbot()