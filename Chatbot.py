def chatbot():
    print("🤖 Simple Chatbot (type 'bye' to exit)")

    while True:
        user_input = input("You: ").lower().strip()

        # Greetings
        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hi!")

        # How are you
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        # Name
        elif user_input == "your name":
            print("Bot: I am a simple chatbot.")

        # Help
        elif user_input == "help":
            print("Bot: You can say hello, hi, hey, how are you, bye")

        # Thanks
        elif user_input in ["thanks", "thank you"]:
            print("Bot: You're welcome!")

        # Time
        elif user_input == "time":
            from datetime import datetime
            print("Bot:", datetime.now().strftime("%H:%M:%S"))

        # Date
        elif user_input == "date":
            from datetime import datetime
            print("Bot:", datetime.now().strftime("%d-%m-%Y"))

        # Exit
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        # Unknown input
        else:
            print("Bot: Sorry, I don't understand.")

# Run chatbot
chatbot()