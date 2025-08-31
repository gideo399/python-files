import random

emojis = { "r" :"🪨", "p":"📄","s" : "✂️"}
choices = ("r","p","s")

while True:
    user_input = input("what do you chose?(r/p/s): ").lower()
    if user_input == "r":
        print("you chose  🪨")
    elif user_input == "s":
        print("you chose ✂️")
    elif user_input == "p":
        print("you chose 📄")
    else: 
        print("invalid alternative ")
        
    sys = ["📄","✂️","🪨"]
    computer_choice = random.choice(sys)
    print(f"computer chose {computer_choice}")

    if user_input == computer_choice:
        print("you won")
    else:
        print("you lose ")
    print  
    













#ROCK PAPER SCISSORS GAME
#   input (rps)
# any input ..
#invalid
#print:
#i chose + input 
#computer chose scissors
#decide winnner

