import re
inputs = {"welcome":r"hi|hello|heyy|good morning|good afternoon|good evening",  "how":r"how are yow|how its going","name":r"tell me your name|who are you" , "bye":"bye|goodbye"}
print("Welcome to autoreply chatbot.How can I help you ? h")
while True:
    user = input()
    if user.lower() in inputs["welcome"]:
        print("Hi,how are you doing?")
    elif user.lower() in inputs["how"]:
        print("Yea..I'm doing great !!")
    elif user.lower() in inputs["name"]:
        print("I'm python chatbot..I dont have any name")
    elif user.lower() in inputs["bye"]:
        print("Goodbye! Have a nice day..")
    response = input("Do you want to continue chat or type bye to exit: ")
    if response.lower() == "bye":
        print("Good bye..Have a nice day")
        break
