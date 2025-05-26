import random

print("\nGuess My Number\n")

print("I am thinking of a number between 0 and 99\n")
random = random.randint(1,99)
correct = False

value = int(input("Enter a guess:"))

if value == random:
    correct = True

if correct:
    print("\nCongrats! The number was:", random)
elif value > random:
    print("\nYour guess is high")
elif value < random:
    print("\nYour guess is low")
while(correct ==  False):

    value = int(input("\nEnter a new number:"))

    if value == random:
        correct = True


    if correct:
        print("\nCongrats! The number was:", random)


    elif value > random:

        print("\nYour guess is high")
    elif value < random:
        print("\nYour guess is low")
