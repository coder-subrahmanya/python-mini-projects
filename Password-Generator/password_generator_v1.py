import random

# Containers
alphabets = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
]
uppercase_alpha = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["@","#","$","&","*","_"]

# User inputs
# Handle invalid entry
while True:
    try:
        length = int(input("Specify the length of the password: "))
        print()
        break
    except:
        print("Invalid operation, try again")
        print()

style = input("Choose preferred password style from these options (numbers/ alphabets/ mixed): ").lower()
print()

# Logic Check
characters = []

if style == "numbers":
    characters = numbers
elif style == "alphabets":
    characters = alphabets + uppercase_alpha

# Confirming Symbols
if style == "mixed":
    characters = alphabets + uppercase_alpha + numbers

    q1 = input("using mixed will add symbols and special characters to password do u want to proceed? (Y/n): ").lower()
    print()

    if q1 == "y": 
        characters = alphabets + numbers + symbols + uppercase_alpha

#Character list check
if len(characters) == 0:
    print("You didn't choose any preference - no password is generated.")
    exit()

# Main Block
password = ""

for i in range(length):
    password += random.choice(characters)

print(f"Your Password is - {password}")
