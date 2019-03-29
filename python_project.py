#Inputs:

age = input("Enter age in years: ")
height = input("Enter height in inches: ")
weight = input("Enter weight rounded to nearest pound: ")
waist = input("Enter waist circumference in inches: ")
blood_sugar = input("Enter measured blood glucose: ")
systolic_bp = input("Enter measured systolic blood pressure: ")
diastolic_bp = input("Enter measured diastolic blood pressure: ")
ex_time = input("Enter daily exercise time in minutes: ")
steps = input("Enter total steps for the day: ")
calories = input("Enter total calorie intake for the day: ")
protein = input("Enter total protein intake for the day in grams: ")
carbs = input("Enter total carbohydrate intak for the day in grams: ")
fat = input("Enter total fat intake for the day in grams: ")
day_md = input("Enter number of days since last MD appointment: ")

BMI = str((int(weight)/2.205)/int((float(height)*float(.0254))*(float(height)*float(.0254))))
print("Your BMI is: ", BMI)
if BMI <= str(24.9):
     print("You're BMI is within normal range.")
else:
    print("You're BMI is above normal range. Consult your physician.")