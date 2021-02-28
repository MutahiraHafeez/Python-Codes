def question_Finder(sentence):
    capital=sentence.capitalize()
    if sentence.startswith(("how","what","where","do","who")):
        return "{}?".format(capital)
    else:
        return "{}.".format(capital)    


newData=[]
while True:
    str = input("Enter a Sentence: ")
    if str=="stop":
        break
    else:
        newData.append(question_Finder(str))    

print(" ".join(newData))
#print(newData)