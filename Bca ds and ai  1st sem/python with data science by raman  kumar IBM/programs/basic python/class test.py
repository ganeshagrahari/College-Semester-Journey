#1-----> write a program to check that person is eligible for vote or not?
'''age = int(input("Enter your age: "))
if age>=18:
    print("You are eligible for vote!")
else:
    print("You are not eligible for vote!") ''' 

#2----> check that person is seinor citizen or not?
'''age = int(input("Enter your age: "))
if age>=60:
    print("You are seinor citizen!")
else:
    print("You are not seinor citizen!") '''

#3----->check the no. entered by user is even or odd?
'''num = int(input("Enter your number: "))
if num%2==0:
    print("The number is even!")
else:
    print("The number is odd!")'''

#4 section planing according to roll no.
'''roll= int(input("Enter your rollno.: "))
if roll<=30:
    print("A section")
elif roll<=60:
    print("B section")
elif roll<=90:
    print("C section")
elif roll<=120:
    print("D section")
else:
    print("E section") '''
#5---->A company decided to give 5% to employee if his/her year of service is more than 5 years ask user for their salary and year of service and print the net bonus ammount?
'''your_salary= int(input("Enter your salary: "))   
your_Service_year= int(input("Enter your service year: "))   
if your_Service_year>5:
      a= (your_salary*(5/100)+your_salary)
    #   print(a)
      print(f"The net bonus is {a-your_salary}")
else:
      print(f"yours net salary is amount is 0")'''      




#6-----> dividing by percentage:---
'''per= int(input("Enter your percentage.: "))
if per>=70:
    print("First division!")
elif per>=50:
    print("Second division!")
elif per>=35:
    print("Third divison!")
else:
    print("FAIL!") '''
#7----->Ticket price is 1000 age 6 to 14 =free, 15 to 25=50% dis., 26 to36=20% dis.,else=10% dis.
print("Ticket price is 1000Rs ")
age= int(input("Enter your age for dicount: "))
if age>=6 and age<=14:
    print("Ticket is free for you!")
if age>=15 and age<=25:
    a= 1000*(50/100)
    print(f"the discount for you is {a} and the net price of your ticket is {1000-a}Rs")
if age>=26 and age<=36:
    b= 1000*20/100
    print(f"the discount for you is {b} and the net price of your ticket is {1000-b}Rs")
else:
    c=1000*(10/100)    
    print(f"the discount  you is {c} and the net price of your ticket is {1000-c}Rs")
    

#8-----> make a calcular using conditional statments  
'''num_1=int(input("Enter the number1: "))
num_2=int(input("Enter the number2: "))
oper= input("Enter any operator(+,-,*,/): ")
if oper== '+':
    print(f"num_1+num_2 is {num_1+num_2}")
elif oper=='-':
    print(f"num_1-num_2 is {num_1-num_2}")    
elif oper=='*':
    print(f"num_1*num_2 is {num_1*num_2}")    
elif oper=='/':
    print(f"num_1*num_2 is {num_1/num_2}")    
else:
    print("Invalid input!!") '''

#9----->Write a program to find that shape is rectangle or square:
'''l=int(input("Enter the length: "))
w=int(input("Enter the width: "))
if l==w:
    print("the shape is square!")
else:
    print("The shape is rectangle")    '''

#10--->take two integer value from user and print greatest among tham:-
'''num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2 : "))
if num1>num2:
    print(f"{num1} is grater")
else:
    print(f"{num2} is greater")  '''

#11---> print the grade  according to the marks gain by the student...
'''marks=int(input("Enter you marks: "))
if marks<25:
    print("F")
elif marks>=25 and marks<45:
    print("E")
elif marks>=45 and marks<50:
    print("D")
eiif marks>=50 and marks<60:
    print("C")
elif marks>=60 and marks<=80:
    print("B")
else:
    print("A")  '''  


#12---> take a age input by three user and print youngest among tham:--
'''per1=int(input("Enter your age per1: "))
per2=int(input("Enter your age per2: "))
per3=int(input("Enter your age per3: "))
if per1<per2 and  per1<per3:
    print("per1 is youngest!")
elif per2<per1 and  per2<per3:
    print("per2 is youngest!")
else:
    print("per3 is youngest!")  '''  

               






