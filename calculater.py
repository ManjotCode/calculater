num1=eval(input("Enter First Number: "))
print("1. Division","2. Floor Division ","3. Multiplication " ,"4. Expoention", "5. Remainder", "6. Addition", "7. Subtraction",sep='\n')
opp=input("Enter [/,//,*,%,+,-]")
num2=eval(input("Enter Second Number: "))

#if number two is Zero
if  opp == 1 and num2 == 0 or opp == '//'and num2 == 0:
    print("ERROR")
    print("Zero cannot be divisible by",num1)

#for diivsion
elif opp == 1 :
    print("=",num1 / num2)

#for Floor Division
elif opp == 2:
    print("=",num1 // num2)

#for Multiplication
elif opp == 3:
    print("=",num1 * num2)

#for Remander
elif opp == 4:
    print("=",num1 % num2)

#for Addition
elif opp == 5:
    print('=',num1 + num2)

#for Subtraction
elif opp == 6:
    print("=",num1 - num2)

#for any error
elif opp == '' and num2 == '' and num1 == '':
    print("Some Thing Whent Wrong ")
