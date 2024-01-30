#BMI CALCULATOR
weight=float(input("enter weight in Kilograms"))
height=float(input("enter height in meters"))
BMI=(weight)/((height**2))
print("BMI:",BMI)
if BMI<=15.9:
    print("Very severely Underweight")
elif 16.0<BMI<16.9:
    print("severely Underweight")
elif 17.0<BMI<18.4:
    print("Underweight")
elif 18.5<BMI<24.9:
    print("Normal")
elif 25.0<BMI<29.9:
    print("Overweitght")
elif 30.0<BMI<34.9:
    print("Obese Class 1")
elif 35.0<BMI<39.9:
    print("Obese Class 2")
elif BMI>=40.0:
    print("Obese Class 3")
else:
    print("Invalid input")