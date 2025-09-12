def showHello():
    print("skibidi bop yes yes yes")
    return 'oh yeah'

def funcA():
    print("Function A is called")
    return 'Function A result' , 999

print(showHello())

data = showHello()
print(data)

info1, info2 = funcA()
print(info1)
print(info2)
