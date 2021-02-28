#myList=[2,3,4,5,6,7,3,8]
#myList.remove(3)
#print(myList)
#print(myList[-4:-2])

temp=[60,90,87]
dic={"a":90,"b":80,"c":70}
def myAvg(data):
    if type(data) == dict:
        avg=sum(data.values())/len(data)
    else:
        avg=sum(data)/len(data)   
    return avg
print(myAvg(dic))        