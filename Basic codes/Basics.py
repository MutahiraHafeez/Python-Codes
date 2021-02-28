import datetime
print(datetime.datetime.now())
data = input()
marks = int(data)
grade = "Null"
if(marks >= 85 and marks <=100):
    grade ='A'
elif(marks >= 80 and marks <=84):
    grade='A-'
elif(marks >= 75 and marks <=79):
    grade='B+' 
elif(marks >= 70 and marks <=74):
    grade='B'    
elif(marks >= 65 and marks <=69):
    grade='B-' 
elif(marks >= 60 and marks <=64):
    grade='C' 
else:
    grade='D'   
print("Grade is :", grade)
