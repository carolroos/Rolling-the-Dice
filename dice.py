import random
#program you'll get a random number between 1-6
roll_again="yes"
while(roll_again=="yes"):
    #random.randint() function will give you a random integer from the specified range
    print(random.randint(1,7))
    roll_again=input("Do you want to roll again:yes or no: ")
