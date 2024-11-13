import hello
import goodbye
import age_func
import binary_game

name = input("What is your name? ")
# say hello when the user starts function
hello.hello(name)

age = input("What is your age? ")
age_func.print_age(age)

# do some stuff
play = input("do you want to play a game? (y/n) ")

if play == "y":
    binary_game.binary_guessing_game()

else :
    print("okay, maybe next time")

# say goodbye when the user ends function
goodbye.goodbye(name)
