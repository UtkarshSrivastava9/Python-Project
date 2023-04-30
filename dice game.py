import random as r
l=[]
while 1:
    n=r.randint(1,6)
    if n==1:
        print('''
    * * * * * * * * *
    *               *
    *               *
    *       O       *
    *               *
    *               *
    * * * * * * * * *
    1️⃣
''')
    elif n==2:
        print('''
    * * * * * * * * *
    *               *
    *               *
    *    O     O    *
    *               *
    *               *
    * * * * * * * * *
    2️⃣
''')
    elif n==3:
        print('''
    * * * * * * * * *
    *               *
    *          O    *
    *       O       *
    *    O          *
    *               *
    * * * * * * * * *
    3️⃣
''')
    elif n==4:
        print('''
    * * * * * * * * *
    *               *
    *    O     O    *
    *               *
    *    O     O    *
    *               *
    * * * * * * * * *
    4️⃣
    ''')
    elif n==5:
        print('''
    * * * * * * * * *
    *               *
    *    O     O    *
    *       O       *
    *    O     O    *
    *               *
    * * * * * * * * *
    5️⃣
''')
    elif n==6:
        print('''
    * * * * * * * * *
    *               *
    *    O     O    *
    *    O     O    *
    *    O     O    *
    *               *
    * * * * * * * * *
    6️⃣
''')
    
    if len(l)<6:
        l.append(n)
    else:
        v=l.pop(0)
        l.append(n)
    ch=input('Do you want to play Again ( Yes or No ) : ').capitalize()
    if ch=='Yes':
        continue
    elif ch =='No':
        break
    else:
        print("Enter a valid choice")