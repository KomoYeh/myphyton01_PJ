print('----------------------------------')
print('Progarm_welcome_student')
print('----------------------------------')

student_name = input("กรุณาป้อนชื่อนักศึกษา: ")
year = input("กรุณาป้อนชั้นปี (ตัวเลข): ")

print(f"ยินดีต้อนรับคุณ {student_name}")

if year == "1":
    print("Welcome Freshman")
elif year == "2":
    print("Welcome Sophomore")
elif year == "3":
    print("Welcome Junior")
elif year == "4":
    print("Welcome Senior")
else:
    print("Oh, no something wrong")
