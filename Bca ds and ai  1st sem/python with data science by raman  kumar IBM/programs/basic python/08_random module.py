#method -->1
''''import random
jackpot = random.randint(1,100)
guess = int(input("chal guess kar: "))
count = 1
while guess!=jackpot: 
    if count>8:
      break
    if guess<jackpot:
        print("Try higher!")
    else:
        print("Try lower!")
    guess=int(input("chal fir se guess kar: ")) 
    count=count+1
if count==9:
   print("You took more than 8 chance! you lost!!")    
else:     
  print("Sahi jawab!") ''' 
#method2---->
import random
jackpot = random.randint(1,100)
print("this is guessing game you have to guess the jackpot number ...the jackpot num lie bw 1 to 100")
guess = int(input("chal guess kar = "))
count = 1
for i in range(8):
 if guess< jackpot:
   print("guess the higher number ")
 elif guess>jackpot:
    print("guess the lower number ")
 else:
   print(f"sahi jawab you took {count} attempts")
 break
 guess = int(input("chal firse guess kar = "))
 count = count+1
else:
  print("you lost the game took more than 8 attempts")
print(" next line of code ")

 
       
    


    