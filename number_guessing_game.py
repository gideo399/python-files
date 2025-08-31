#Number guessing game 
import random 
#system guess 
system_guess =random.randint(1,100)
# allow user to input a guess
while True:
    try:
     user_guess=int(input("what is your guess?: "))
    except ValueError:
        print("onvalid input only numbers are allowed ")
# if the user guess == the computer guess
    if user_guess == system_guess:
        print("congratulation..You've got the guess")
#else if guess is greater than the system guess print toohigh
    elif user_guess > system_guess:
        print("Too high ")
#elif if it is low print
    elif user_guess < system_guess:
        print("too low ") 
#print too low 
    else:
        print("invalid input ")
#terminate 
    