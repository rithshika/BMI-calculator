#BMI Calculator

print('Welcome to the BMI Calculator')

#Get user input
weight = float(input('Enter your weight in kilograms(kg): '))
height = float(input('Enter your height in meters(m): '))

#calculate BMI
bmi = weight/(height ** 2)

#display BMI
print(f"Your BMI is: {bmi:.2f}")

# Interpret BMI
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
