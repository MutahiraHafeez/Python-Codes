def estimate(a):
    if a>5:
        print("Greater")
    else:
        print("Less")

def estimate1(a):
    if a>5:
        return "Greater"
    else:
        return "Less"

data = float(input("Enter Some Value: "))
estimate(data)
print("-----------------")
print(estimate1(data))

