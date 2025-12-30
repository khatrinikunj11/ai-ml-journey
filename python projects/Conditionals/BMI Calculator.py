weight = input("Enter your weight in kg: ")
height = input("Enter your height in meters: ")
bmi = float(weight) / (float(height) ** 2)
print("Your BMI is: " + str(bmi))
if bmi < 18.5:
    print("You are underweight. You should eat more.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight. Good job!")
elif 25 <= bmi < 29.9:
    print("You are overweight. You should consider losing some weight.")