import hello
import goodbye
import age_func

name = input("What is your name? ")
# say hello when the user starts function
hello.hello(name)

age = input("What is your age? ")
age_func.print_age(age)

# do some stuff
i = 0
while i < len(name):
    print(name[i])
    i += 1

# say goodbye when the user ends function
goodbye.goodbye(name)
