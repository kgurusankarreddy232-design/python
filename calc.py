#SIMPLE CALCLATOR


num1=int(input('THE VALUE OF A:'))

num2=int(input('THE VALUE OF B:'))

operator=input('ENTER THE OPERATOR {ONLY +,-,*,/,%}: ')

#ENTER ONLY +,-,*,**,/

if operator == "+":
   print(num1+num2)

elif operator == "-" :
   print(num1-num2)

elif operator=="*":
   print(num1*num2)

elif operator == "/":
   print(num1/num2)

elif operator == "%":
   print(num1%num2)

