def countChar(str,count=0):
    if count == len(str):
        return 0
    return 1 + countChar(str,count+1)

print("Total Characters are:",countChar("Mutahira"))    

def findMax(L,size):
    if size<=0:
        return -1
    val=int(findMax(L,size-1))
    if val<L[size]:
        val=L[size]
    return val

l=[1,3,4,1,18,7,6]
print(findMax(l,5))  

def searchByBinary(lst,start,end,key):
    if start>end:
        return -1
    mid = (end + start) // 2
    if lst[mid]==key:
        return mid
    elif lst[mid] > key:
        return searchByBinary(lst,start,mid-1,key)
    else:
        return searchByBinary(lst,mid+1,end,key)  

lst=[1,2,3,4,5,6,7,8,9,10]
try:
    print("Search Index is: ",searchByBinary(lst,0,10,10))
except Exception:
    print("Unexpected Error Occured!")    

         

