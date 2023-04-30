import random


n=random.randint(1,100)

print("Aur Bhai Ek Game Ho Jaye".center(100))
o=input("Enter Yes or No : ")

if o=="Yes" :
    att=input("Kripya Apna Level Bataiye  : | Bot | Noob | Pro | Hacker | ")

    if att=="Bot":
        chance=10
    elif att=="Noob":
        chance=8
    elif att=="Pro":
        chance=6
    elif att=="Hacker":
        chance=3





else :
    chance=0

while chance:
    guess=int(input("Guess the Number "))

    if guess>n:
        print("Jyada Ho Gya")
        print("Chance remaining : ",(chance-1))

    elif guess<n:
        print("Kam Ho Gya")
        print("Chance remaining : ",(chance-1))
    elif guess==n:
        print(" 7 CRORE 😊😊😊😊😊")
        break

    chance=chance-1

else :
    print("Sorry Bro The Number Was : ",n)
    print("Better Luck Next Time")
