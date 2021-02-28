#a='a'
#b='@'
#password = 'mutahira'
#print("Before: ",password)
#password=password.replace(a,b)
#print("After: ",password)

SECURE = (('A','/|'),('M','|\/|'),('u','(_)'),('i','!'),('a','@'),('O','0'),('D','|)'),('K','|<'))

def passwordsecure(password):
    for a,b in SECURE:
        password = password.replace(a,b)
    
    return password

password = input("Please provide your password here: ")
decision = input("Do you need UPPER case letters to be present? (y/n)")

if decision == 'y':
    print(f"Your new password is {passwordsecure(password)}")
else:
    print(f"Your new password is {passwordsecure(password.lower())}")