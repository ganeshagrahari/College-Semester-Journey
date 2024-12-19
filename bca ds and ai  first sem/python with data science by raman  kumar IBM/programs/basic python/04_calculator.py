# num_1=int(input("Enter the number1: "))
# num_2=int(input("Enter the number2: "))
# oper= input("Enter any operator(+,-,*,/): ")
# if oper== '+':
#     print(f"num_1+num_2 is {num_1+num_2}")
# elif oper=='-':
#     print(f"num_1-num_2 is {num_1-num_2}")    
# elif oper=='*':
#     print(f"num_1*num_2 is {num_1*num_2}")    
# elif oper=='/':
#     print(f"num_1*num_2 is {num_1/num_2}")    
# else:
#     print("Invalid input!!")    
email=input("apna email bta: ") 
password=input("apna password bhi bta: ") 
if email=='Pyhton@gmail.com'and password=='1234':
       print("login") 
elif email=='python@gmail.com' and password !='1234':
       print ("wrong password ") 
       password=input("phirse password bharo") 
       if password=='1234':
         print(" login ") 
       else:
         print(" still wrong password ")