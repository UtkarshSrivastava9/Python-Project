import random
a=["ROCK","PAPER","SCISSORS"]
print("WELCOME TO THE GAME OF ROCK PAPER SCISSORS   🪨   🧻   ✂️")

ai=random.choice(a)

g=int(input(''' ROCK KE LIYE 1 DABAYEN 
                PAPER KE LIYE 2 DABAYEN 
                STONE KE LIYE 3 DABAYEN '''))

if g==1:
    ch="ROCK"
elif g==2:
    ch="PAPER"
elif g==3:
    ch="SCISSORS"



if ai==ch:
    print(" THE MATCH IS DRAW ")
else:
    if (ai=="ROCK" and ch=="PAPER") or (ai=="PAPER" and ch=="SCISSORS") or (ai=='SCISSORS' and ch=='ROCK'):
        print("Tera : ",ch)
        print("Mera : ",ai)
        print('AAP MUMBAI AA SAKTE HAI   🍾🥂')
    else :
        print("Tera : ",ch)
        print("Mera : ",ai)
        print("You Loose")

