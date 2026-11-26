
# BODY MASS INDEX (BMI) CALCULATOR

print("To Calculate Your BMI, Please Enter Your Details Below")

name = input("Enter Your Name: ")
age = input("Enter Your Age: ")

try:
    weight = float(input("Enter your weight in Kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be greater than zero.")

    else:
        BMI = weight / (height ** 2)
        round_value = round(BMI, 1)

        print(f"\nBMI: {round_value}")

        print()
        print(
            f"Name: {name}\n"
            f"Age: {age}\n"
            f"Weight: {weight} kg\n"
            f"Height: {height} m\n"
            f"BMI: {round_value}"
        )

        # BMI Classification
        if round_value < 16.0:
            print("You are severely thin!")

        elif round_value < 17.0:
            print("You have moderate thinness!")

        elif round_value < 18.5:
            print("You have mild thinness!")

        elif round_value < 25.0:
            print("You are in normal weight range.")

        elif round_value < 30.0:
            print("You are overweight!")

        elif round_value < 40.0:
            print("You are in obesity category!")

        else:
            print("You are in severe obesity category!")

except ValueError:
    print("Please enter valid numerical values for weight and height.")
