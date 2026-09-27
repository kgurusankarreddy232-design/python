num1=int(input("ENTER THE VALUE A:"))
num2=int(input("ENTER THE VALUE B:"))
num3=int(input("ENTER THE VALUE C:"))
if num1>num2>num3:
    print(num1)
elif num2>num3<num1:
    print(num2)
elif num3>num2>num1:
    print(num3)
else:
    print("equal")