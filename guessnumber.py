import random

n=random.randint(1,99)
  
guess=int(input("Enter a number"))

while True:
   if guess<n:
    print("Guess is low")
    guess=int(input("Enter a number"))

   elif guess>n:
    print("Guess is high")
    guess=int(input("Enter a number"))

   else:
    print("Congratulation you are right")
    break