import random

response = "n"

while response != "y":
    response = input("do you want to roll a dice? (y/n)")

while response =="y":
   dice = random.randint(1,6)
   if dice == 1:
        print("You rolled 1")
        response = input("do you want to continue? (y/n)")
   elif dice == 2:
        print("You rolled 2")
        response = input("do you want to continue? (y/n)")
   elif dice == 3:
        print("You rolled 3")
        response = input("do you want to continue? (y/n)")
   elif dice == 4:
        print("You rolled 4")
        response = input("do you want to continue? (y/n)")
   elif dice == 5:
        print("You rolled 5")
        response = input("do you want to continue? (y/n)") 
   elif dice == 6:
        print("You rolled 6")
        response = input("do you want to continue? (y/n)")

