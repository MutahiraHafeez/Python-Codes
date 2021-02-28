#For Loop with list
numbers =[10.39,10.56,19.45,56.49]

for i in numbers:
    print(round(i))

#Foor loop with dictionary

temp ={"a":20.12,"b":40.56,"c":90.00}

for i in temp.items():
    print(i)

for i in temp.keys():
    print(i)   

for i in temp.values():
    print(round(i))     

#While loop examples 
#Example 1
a=19
while a>10:
    print(a)
    a=a-1
#Example 2
password=input("Enter your Password: ")
while password!="890":
    password=input("Wrong Password! Enter again: ")
    
#Example 3
password2=input("Enter your Password: ")
while True:
    if(password2 != "888"):
        password2=input("Wrong Password! Enter again: ")
        continue
    else:
        print("Password Matched! Thank you")
        break    






    

