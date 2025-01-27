#SIMPLE CALCULATOR

print("select the option what to want to calculate")

def caculator():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choose=input("Enter the choise number you want to calculate (1/2/3/4): ")

    if choose in ['1','2','3','4']:
        a=float(input("Enter the number a:"))
        b=float(input("Enter the number b:"))


        if choose=='1':
            print(f"The solution of addition is = {a+b}")   

        elif choose=='2':
            print(f"The solution is subtraction is = {a-b}")

        elif choose=='3':
            print(f"The solution is Multiplication is = {a*b}")

        elif choose=='4':
            try:
               print(f"The solution is Division is = {a/b}")
            except ZeroDivisionError:
               print("b cannot be zero! infinite solution!")      

    else:
        print("Enter a proper number")

caculator()   
 