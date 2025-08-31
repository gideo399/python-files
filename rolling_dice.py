import random

def random_number():
    attempt = 0
    score = 0
    attempt_max = 3

    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    while True:
        choice = input("roll a die?(y/n): ").lower()
       
            
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"{die1},{die2}")
        elif choice =="n":
        print("thank you")
        break   
    else:
            
        print("invalid ")
random_number():

