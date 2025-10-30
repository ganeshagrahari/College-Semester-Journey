<<<<<<< HEAD
import random
randno= random.randint(1,100)
guess =int(input("enter your no.: "))
count = 1
while guess!=randno:
    if count>8:
        break
    if guess>randno:
        print("Try lower!")
    else:
        print("try hingher!")  
    guess=int(input("enter your no.: "))
    count=count+1
if guess==9:
    print("you lost you took more than 8 chance")  
else:
    print(f"sahi jawab! and you take {count} chance!")       
=======
import random
randno= random.randint(1,100)
guess =int(input("enter your no.: "))
count = 1
while guess!=randno:
    if count>8:
        break
    if guess>randno:
        print("Try lower!")
    else:
        print("try hingher!")  
    guess=int(input("enter your no.: "))
    count=count+1
if guess==9:
    print("you lost you took more than 8 chance")  
else:
    print(f"sahi jawab! and you take {count} chance!")       
>>>>>>> dc4cba81a1c391062d7063dbe308d4162a8a9149
