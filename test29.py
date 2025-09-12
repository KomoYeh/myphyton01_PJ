def showpgname():
    print("----------------------")
    print("cabondioxide_calculator")
    print("----------------------")

def showresult(car_owner, car_number, car_carbon, status):
    print(f'Owner: {car_owner}')
    print(f'Car Number: {car_number}')
    print(f'Carbon Emission: {car_carbon} g/km')
    print(f'Status: {status}')


def inputData():
    car_owner = input("Enter your name: ")
    car_number = input("Enter your car number: ")
    car_carbon = float(input("Enter your car carbon dioxide emission (grams/km): "))
    return car_owner, car_number, car_carbon

def calculateCarbonEmission(car_owner, car_number, car_carbon) :
    if car_carbon > 678.55 :
        #ผ่าน
        showresult(car_owner, car_number, car_carbon, 'Pass')
    else :
        #ไม่ผ่าน
        showresult(car_owner, car_number, car_carbon, 'Fail')

def showpa():
    print("-----------------------")

 