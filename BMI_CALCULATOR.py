#BODY MASS INDEX (BMI)CALCULATOR

print("To Calculate Your BMI Please Enter Your Given Details Below ")

name=input("Enter Your Name :")
age=input("Enter Your Age :")

try:
     weight=float(input("Enter your weight in Kilograms(kg) :"))
     height=float(input("Enter your height in meters(m) :")) 

     BMI=weight/(height**2)

     round_value=round(BMI,1)

     print (f"BMI:{round_value}")

     print()

     print(f"Name:{name}\nAge:{age}\nWeight:{weight}\nHeight:{height}\nBMI:{round_value}")

     if round_value <18.5:     
         print("Your are Underweight!")

     elif 16.0<=round_value<17.0:
         print("You have moderate Thinness!")

     elif 17.0<=round_value<18.5:
         print("You have mild Thinness!")

     elif 18.5<=round_value<25.0:
         print("Your are in Normal Weight.")

     elif 25.0<=round_value<30.0:
         print("You are overweight!")

     elif 30.0<=round_value<40.0:
         print("You are in OBESITY CATEGARY!")    

     else:
         print("You are in a severe obesity categary")

except ZeroDivisionError:
    print("Height cannot be Zero, please enter a proper number")

except ValueError:
    print("Enter a proper number please!")

except TypeError:
        print("Enter a proper number please!")
   
