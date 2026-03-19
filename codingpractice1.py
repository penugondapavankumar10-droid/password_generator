number=int(input("Enter a number: "))
Sum=0
while True:
    Sum+=number
    number = int(input("Enter a number: "))
    if number==0:
        break
else:
    print("Else Block")
print("Total Sum is",Sum)
