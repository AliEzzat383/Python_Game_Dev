def x(a,b):
    return a+b
def y(a,b):
    return a-b

def calc(u,v):
    reply=input("use op")
    if reply == "x":
        return x(u,v)
    elif reply == "y":
        return  y(u,v)
def wow():
    print("wow")
wow


print(calc(1,2,"x"))