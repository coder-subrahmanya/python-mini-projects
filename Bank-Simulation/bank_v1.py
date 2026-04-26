current_balance = 0
pin = 462003
attempt = 3
last_deposit = 0
last_withdraw = 0
daily_limit = 5000
total_withdraw = 0
answer_1 = "guest"
answer_2 = "guest"

#HEADER BLOCK
print("======================")
print("   Section C's BANK ")
print("======================")
print(" ")

#WELCOME BLOCK
name = input("Enter your name: ").title()
print(f"Welcome to Section Cs Bank Interface {name}!")
print()

#LOGIN BLOCK
while True:
  login = int(input("Enter the pin to access your account: "))

  if pin == login:
      print()
      print("Access granted!")
      print()
      break
  
  elif pin != login:
      attempt -= 1
      print()
      print("Access denied, try again")
      print()

#ATTEMPT ENDING AND PIN RESET BLOCK
      if attempt == 0:
        reset = input("Account is locked after many failed attempts, Do u want to reset your pin? (Y/n): ").lower()

        #RESET PIN
        if reset == "y":
            print()
            print("Answer these security questions to reset password")
            print()

        #SECURITY QUESTIONS
            question_1 = input("What is Shruti's fav food? ").lower()
            print()
            question_2 = input("Who is Shruti's fav teacher? ").lower()

            #ANSWER CHECK
            if question_1 == answer_1 and question_2 == answer_2:
                print()
                change_pass = int(input("Enter your new pin: "))
                print()
                pin = change_pass     

        elif reset == "n":
                exit()

        continue

#MENU BLOCK
print("===MENU===")
print("""1. Check Balance
2. Deposit
3. Withdraw
4. Mini Statement
5. Logout""")

#MAIN OPERATION BLOCK
while True:
  print()
  operations = int(input("Choose your operation(1-5): "))
  print()

  if operations == 1:
      print(f"Your account balance is ${current_balance}")
      print()

#DEPOSIT BLOCK
  elif operations == 2:
      deposit = int(input("Enter the amount to deposit: "))
      
      current_balance += deposit
      last_deposit = deposit
      
      print()
      print(f"Amount of ${deposit} is credited to your account!")
      print()

#WITHDRAW BLOCK  
  elif operations == 3:
      withdraw = int(input("Enter the amount to withdraw: "))

    #WITHDRAW AMOUNT CHECK
      if current_balance < withdraw:
          print("You don't have enough amount in account to withdraw!")

      elif current_balance >= withdraw:

        #WITHDRAW CONFIRMATION          
          confirmation = input(f"Are u sure u want to withdraw {withdraw}? (Y/n)").lower()
          print()

          if confirmation == "y":

            #WITHDRAW LIMIT CHECK
            if withdraw > daily_limit:
                print("You can't withdraw because daily limit.")
                continue
            
            daily_limit -= withdraw
            last_withdraw = withdraw
            current_balance -= withdraw

            print(f"Amount of ${withdraw} is debited from your account!")

          elif confirmation == "n":
              print("Transcation Cancelled")
              print()

#MINI STATEMENT BLOCK
  elif operations == 4:
      
      #TRANSACTION CHECK
      if last_deposit == 0 and last_withdraw == 0:
          print()
          print("No transactions yet")
          continue
      
      print()
      print("---Mini Statement---")
      print(f"Last deposit: ${last_deposit}")
      print(f"Last withdraw: ${last_withdraw}")

#EXIT BLOCK
  elif operations == 5:
      print(f"Thank you for visiting us!, your last balance was ${current_balance}")
      break
