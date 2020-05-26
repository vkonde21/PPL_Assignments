#guess number

import random
n = random.randint(1, 100)
guess = int(input("Enter an integer from 1 to 100: "))
#first chance is over here
c = 10
flag = 1
while c > 1:
    if guess < n:
        print("Your guess is low")
        guess = int(input("Enter an integer from 1 to 100: "))
    elif guess > n:
        print("Your guess is high")
        guess = int(input("Enter an integer from 1 to 100: "))
    else:
        print("Correct guess")
        flag = 0
        break
    c = c - 1
if(flag == 1):
    print("Your chances are over")

