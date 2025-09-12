def funcA(n1, n2) :
    print('hehe')
    return n1 + n2

def funcB(data1, data2, data3):
    result = data1 * data2
    return result, data3 + result

print(funcA(10, 20))

iot01 = funcA(5, 10)
print(iot01)

aa, bb = funcB(10, 20, 30)
print(aa)
print(bb)