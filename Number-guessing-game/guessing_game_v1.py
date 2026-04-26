#Guess The Number Game
import random
import time

count = 0
max_tries = 7
secret_number = 0

start = input("Press 'enter' to start the game: ")
print()
time.sleep(1.5)

print("""Hello User!, Welcome to Guessing Game
Before we start - select the difficulty down below
""")
print()
time.sleep(1)

print("""-----Difficulties-----
1. Easy (1-20)
2. Medium (1-50)
3. Hard (1-100)
-------------------------
""")
print()
time.sleep(1)

while True:
    try:
        user_def_choice = int(input("Choose your difficulty (1-3): "))
        print()
    except ValueError:
        print("Invalid entry try again")
        print()
        continue

    if user_def_choice >= 4:
        print("Invalid try again")
        print()
    elif user_def_choice == 0:
        print("Invalid try again")
        print()
    else:
        break 

if user_def_choice == 1:
    secret_number = random.randint(1,20)
elif user_def_choice == 2:
    secret_number = random.randint(1,50)
else:
    secret_number = random.randint(1,100)

print("Game begins in...")

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

while True:
    count += 1

    try:
        guess = int(input("Guess the number: "))
        print()
    except ValueError:
        print("That's not a valid number")
        print()
        continue

    max_tries -= 1
    
    if guess == secret_number:
        print("You Won!!")
        print()
        print(f"Number of tries you took: {count}")
        break

    elif guess < secret_number:
        print("Too low!")
        print()

    elif guess > secret_number:
        print("Too high!")
        print()

    else:
        print("Invalid..")
        print()

    if max_tries == 0:
        print(f"You loose, the number was {secret_number}.")
        print()
        break
