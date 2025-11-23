#Greetings and User Info
def GreetUser():
    print("---Welcome to GenZ Life Simulator---")
    name = input("What's your name? ")
    age = input("How old are you? ")
    user = {"name": name, "age": age}
    print("Hi,", name, "I am your new buddy now.")
    return user



#Responses Function and Keys
responses = {"hi": "Hey bestie!","how are you": "I’m vibing, wbu?","bye": "Aww, see you soon"}

def GetResponse(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return responses[user_input]
    else:
        return "Hmm… idk what to say"



#End of chat
def EndChat():
    print()
    print("===================")
    print("Chat ended!")
    print("Take care Buddy")
    print("===================")



#Game Stats Display
def ShowStatus(energy, mood, points):
    print("---------------------------")
    print("\nCurrent Stats:")
    print("Energy:", energy)
    print("Mood:", mood)
    print("Points:", points)
    print("---------------------------")




#Game Updates
def UpdateStats(choice, energy, mood, points):
    if choice == "study" or choice =='1':
        energy -= 20
        points += 10
        mood = "Hardwork on its peak"
    elif choice == "eat" or choice == '2':
        energy += 15
        mood = "Yummy ;)"
    elif choice == "play" or choice == '3':
        energy -= 10
        points += 5
        mood = "What a match!"
    elif choice == "sleep"or choice =="4":
        energy = 100
        mood = "Did I take a nap or was it a hibernation =o"
    else:
        print("Invalid choice")
    if energy > 100:
        energy = 100

    return energy, mood, points



#Display the points
def EndGame(points):
    print()
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Game Over")
    print("You earned", points, "points in your GenZ Life!")
    print("See ya next time bestie")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print()





#Chat Loop
def ChatLoop(user):
    print(" ___________________________________________________________")
    print("|type 'bye' to end                                          |")
    print("|type 'game' to play game                                   |")
    print("|___________________________________________________________|")
    print()
    print(">>>>CHAT WITH ME BRO!<<<<")
    while True:
        user_input = input("You: ").lower()

        if user_input=="game":
            print("That's what i like buddy. You are a fun person XD")
            ans = input("Shall we start? (Yes/No)").lower()
            if ans == "yes":
                result = StartGame(user)
                if result == -1:
                    return ChatLoop(user)
                continue
            else:
                print("Aww okay, let's keep chatting ")
                continue



        print("Bot:", GetResponse(user_input))
        if user_input == "bye":
            EndChat()
            break




#Mini Game
def StartGame(user):
    print()
    print("Welcome to Mini Game", user["name"])
    energy = 100
    mood = "Excited"
    points = 0

    while energy>0:
        ShowStatus(energy, mood, points)
        print()
        print("Choose an activity:")
        print("1. study")
        print("2. eat")
        print("3. play")
        print("4. sleep")
        print("5. quit")

        choice = input("Enter your choice: ").lower()

        if choice == "quit" or choice == "5":
            EndGame(points)
            return -1
        else:
            energy, mood, points = UpdateStats(choice, energy, mood, points)

        if energy <= 0:
            print(">>> You ran out of energy!")
            print(">>> Why do you play and study this much bro?")
            print(">>> dont you have a life!?")
            print("    :(   ")
            return -1



#Main Program1
user = GreetUser()
ChatLoop(user)
