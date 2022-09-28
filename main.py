# first project in my 200 python project series
# LOTTO GAME (PROGRAM TO CHOOSE A RANDOM WINNER
import random

num_1 = random.randint(1, 20)
predict_number = int(input("Enter your Lotto Number: "))
if predict_number == num_1:
    print("Congratulations 🎈🎈🎈🎉. YOU HAVE WON")
else:
    print("Sorry, TRY AGAIN")
