#Inputs:

age = input("Enter age in years: ")
gender = input("Enter gender (male/female): ")
height = input("Enter height in inches: ")
weight = input("Enter weight rounded to nearest pound: ")
waist = input("Enter waist circumference in inches: ")
blood_sugar = input("Enter measured blood glucose: ")
systolic_bp = input("Enter measured systolic blood pressure: ")
diastolic_bp = input("Enter measured diastolic blood pressure: ")
activity_level = input("Enter activity level; sedentary (little or no exercise), lightly active (light exercise/sports 1-3 days/week), moderatetely active (moderate exercise/sports 3-5 days/week), very active (hard exercise/sports 6-7 days a week), extra active (very hard exercise/sports & physical job or 2x training): ")
ex_time = input("Enter daily exercise time in minutes: ")
steps = input("Enter total steps for the day: ")
calories = input("Enter total calorie intake for the day: ")
protein = input("Enter total protein intake for the day in grams: ")
carbs = input("Enter total carbohydrate intake for the day in grams: ")
fat = input("Enter total fat intake for the day in grams: ")
day_md = input("Enter number of days since last MD appointment: ")

print()
#BMI=Body Mass Index
BMI = str((int(weight)/2.205)/int((float(height)*float(.0254))*(float(height)*float(.0254))))
print("Your BMI is: ", BMI)
print()
if BMI <= str(24.9):
     print("You're BMI is within normal range.")
else:
     print("You're BMI is above normal range. Consult your physician.\n")
     print("For helpful weight management information, visit: ", "http://www.cdc.gov/healthyweight/effects/index.html")

print()
#BMR=Basal Metabolic Rate

if gender == "female":
     BMR = str(655 + int(4.35 * float(weight)) + int(4.7 * float(height)) - int(4.7 * float(age)))
     print("Your BMR is: ", BMR)
else:
     BMR = str(66 + int(6.23 * float(weight)) + int(12.7 * float(height)) - int(6.8 * float(age)))
     print("Your BMR is: ", BMR)

print()
print("You're reported calorie intake for the day is", calories)

print()
#TDC=Total Daily Calories to maintain weight based on Harris Benedict Equation

if activity_level == "sedentary":
     TDC = str(float(BMR) * float(1.2))
     print("The daily total number of calories you need in order to maintain your current weight is", TDC)
elif activity_level == "lightly active":
     TDC = str(float(BMR) * float(1.375))
     print("The daily total number of calories you need in order to maintain your current weight is", TDC)
elif activity_level == "moderately active":
     TDC = str(float(BMR) * float(1.55))
     print("The daily total number of calories you need in order to maintain your current weight is", TDC)
elif activity_level == "very active":
     TDC = str(float(BMR) * float(1.725))
     print("The daily total number of calories you need in order to maintain your current weight is", TDC)
elif activity_level == "extra active":
     TDC = str(float(BMR) * float(1.95))
     print("The daily total number of calories you need in order to maintain your current weight is", TDC)
else:
     print("Invalid entry.")

print()
print("The daily total number of calories you need to lose about 1 pound per week is", str(float(TDC)-float(500.0)))

print()
print("The daily total number of calories you need to gain about 1 pound per week is", str(float(TDC)+float(500.0)))

print()
#BFP = estimated Body Fat Percentage

if gender == "female":
     BFP = str(float(1.20) * float(BMI) + float(0.23) * float(age) - float(5.4))
     print("You're estimated body fat percentage is",BFP)
else:
     BFP = str(float(1.20) * float(BMI) + float(0.23) * float(age) - float(16.2))
     print("You're estimated body fat percentage is",BFP)

print()
#SBP = systolic blood pressure
#DSP = diastolic blood pressure

if systolic_bp <= "120" and diastolic_bp <= "80":
     print("Your blood pressure at ", systolic_bp,"/",diastolic_bp, " is optimal.")
elif systolic_bp >= "121" <= "129" or diastolic_bp <= "79":
     print("Your blood pressure at ", systolic_bp,"/",diastolic_bp, " is elevated. Schedule an appointment to see your physician.")
elif systolic_bp >= "130" <= "139" or diastolic_bp >= "80" <= "89":
     print("Your blood pressure at ", systolic_bp,"/",diastolic_bp, " is Stage 1 hypertension. Contact your physician.")
elif systolic_bp >= "140" <= "179" or diastolic_bp >= "90" <= "119":
     print("Your blood pressure at ", systolic_bp,"/",diastolic_bp, " is Stage 2 hypertension. Contact your physician.")
elif systolic_bp >= "180" <= "200" or diastolic_bp >= "120" <= "150":
     print("Your blood pressure at ", systolic_bp,"/",diastolic_bp, " indicates a hypertensive crisis. Dial 911 or proceed to emergency room.")
else:
     pass

#the optimal and elevated conditions work but Stage 1, Stage 2, and Crisis don't. Still working on it.
