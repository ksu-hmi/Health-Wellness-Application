#Inputs:

age = input("Enter age in years: ")
gender = input("Enter gender (male/female): ")
height = input("Enter height in inches: ")
weight = input("Enter weight rounded to nearest pound: ")
waist = input("Enter waist circumference in inches: ")
blood_sugar = input("Enter measured blood glucose: ")
systolic_bp = input("Enter measured systolic blood pressure: ")
diastolic_bp = input("Enter measured diastolic blood pressure: ")
activity_level = input("Enter activity level; sedentary (little or no exercise), lightly active (light exercise/sports 1-3 days/week), moderately active (moderate exercise/sports 3-5 days/week), very active (hard exercise/sports 6-7 days a week), extra active (very hard exercise/sports & physical job or 2x training): ")
ex_time = input("Enter daily exercise time in minutes: ")
steps = input("Enter total steps for the day (No commas): ")
calories = input("Enter total calorie intake for the day (No commas): ")
day_md = input("Enter number of days since last MD appointment: ")

print()
#BMI=Body Mass Index
BMI = str(int(float(weight)*float(703))/int((float(height)*float(height))))
print("Your BMI is: ", BMI[0:4])
print()
if BMI <= str(18.4):
     print("BMI is your Body Mass Index. Your BMI is below normal range. Consult your physician.\n")
     print("For helpful weight management information, visit: ", "http://www.cdc.gov/healthyweight/effects/index.html")
elif BMI >= str(18.5) and BMI <= str(24.9):
     print("BMI is your Body Mass Index. Your BMI is within normal range.")
else:
     print("BMI is your Body Mass Index. Your BMI is above normal range. Consult your physician.\n")
     print("For helpful weight management information, visit: ", "http://www.cdc.gov/healthyweight/effects/index.html")

print()
#BMR=Basal Metabolic Rate

if gender == "female":
     BMR = str(655 + int(4.35 * float(weight)) + int(4.7 * float(height)) - int(4.7 * float(age)))
     print("BMR is your Base Metabolic Rate, the amount of daily calories your body burns at rest. Your BMR is: ", BMR)
elif gender == "male":
     BMR = str(66 + int(6.23 * float(weight)) + int(12.7 * float(height)) - int(6.8 * float(age)))
     print("BMR is your Base Metabolic Rate, the amount of daliy calories your body burns at rest. Your BMR is: ", BMR)
else:
     print("Invalid gender, weight, height, or age entry.")

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
     print("Invalid entry for activity level.")

print()
print("The daily total number of calories you need to lose about 1 pound per week is", str(float(TDC)-float(500.0)))

print()
print("The daily total number of calories you need to gain about 1 pound per week is", str(float(TDC)+float(500.0)))

print()
#BFP = BMI estimated Body Fat Percentage (https://www.calculator.net/body-fat-calculator.html)

if gender == "female":
     BFP = str(float(1.20) * float(BMI) + float(0.23) * float(age) - float(5.4))
     print("You're estimated body fat percentage is",BFP[0:5])
else:
     BFP = str(float(1.20) * float(BMI) + float(0.23) * float(age) - float(16.2))
     print("You're estimated body fat percentage is",BFP[0:5])

print()
print("For a healthy body-fat scale reference, visit: ", "https://www.acefitness.org/education-and-resources/lifestyle/tools-calculators/percent-body-fat-calculator")

print()
#WHR = Waist to Height Ratio

if gender == "male":
     WHR = str(int(waist)/int(height))
     if WHR <= str(float(.42)):
          print("Your waist to height ratio of", WHR[0:4], "indicates that you may be underweight. Consider healthier choices and consult your physician.")
     elif WHR >= str(float(.43)) and WHR <= str(float(.52)):
          print("Your waist to height ratio of", WHR[0:4], "indicates that you are at a healthy weight. Continue to maintain a healthy lifestyle.")
     elif WHR >= str(float(.53)) and WHR <= str(float(.62)):
          print("Your waist to height ratio of", WHR[0:4], "indicates that you may be overweight. Consider healthier choices and consult your physician.")
     elif WHR >= str(float(.63)):
          print("Your waist to height ratio of", WHR[0:4], "indicates that you may be obese and at greater risk for health issues. Consider healthier choices and consult your physician.")
     else:
          print("Unusual result: Re-enter waist and height values.")

elif gender == "female":
     WHR = str(int(waist)/int(height))
     if WHR <= str(float(.41)):
          print("Your waist to height ratio of", WHR[0:4], "indicates that you may be underweight. Consider healthier choices and consult your physician.")
     elif WHR >= str(float(.42)) and WHR <= str(float(.48)):
          print("Your waist to height ratio of", WHR[0:4], "indicates that you are at a healthy weight. Continue to maintain a healthy lifestyle.")
     elif WHR >= str(float(.49)) and WHR <= str(float(.57)):
          print("Your waist to height ratio of", WHR[0:4], "indicates that you may be overweight. Consider healthier choices and consult your physician.")
     elif WHR >= str(float(.58)):
          print("Your waist to height ratio of", WHR[0:4], "indicates that you may be obese and at greater risk for health issues. Consider healthier choices and consult your physician.")
     else:
          print("Unusual result: Re-enter waist and height values.")

else:
     print("Unusual Waist-to-Height Ratio result: Check for accurate gender, height, and weight values entered.")

print()
print("For more educational information on Waist-to-Height Ratio, visit", "http://prowellness.vmhost.psu.edu/families/understanding_risk/whtr")

print()
#SBP = systolic blood pressure
#DSP = diastolic blood pressure

if int(systolic_bp) <= 89 and int(diastolic_bp) <= 59:
     print("Your blood pressure at ", systolic_bp,"/",diastolic_bp, " is possibly low. Contact your physician.")
elif int(systolic_bp) >= 90 and int(systolic_bp) <= 120 and int(diastolic_bp) >= 60 and int(diastolic_bp) <= 80:
     print("Your blood pressure at ", systolic_bp,"/",diastolic_bp, " is optimal.")
elif int(systolic_bp) >= 121 and int(systolic_bp) <= 129 and int(diastolic_bp) <= 79:
     print("Your blood pressure at ", systolic_bp,"/",diastolic_bp, " is elevated. Schedule an appointment to see your physician.")
elif int(systolic_bp) >= 130 and int(systolic_bp) <= 139 and int(diastolic_bp) >= 80 and int(diastolic_bp) <= 89:
     print("Your blood pressure at ", systolic_bp,"/",diastolic_bp, " is Stage 1 hypertension. Contact your physician.")
elif int(systolic_bp) >= 140 and int(systolic_bp) <= 179 and int(diastolic_bp) >= 90 and int(diastolic_bp) <= 119:
     print("Your blood pressure at ", systolic_bp,"/",diastolic_bp, " is Stage 2 hypertension. Contact your physician.")
elif int(systolic_bp) >= 180 and int(systolic_bp) <= 200 and int(diastolic_bp) >= 120 and int(diastolic_bp) <= 150:
     print("Your blood pressure at ", systolic_bp,"/",diastolic_bp, " indicates a hypertensive crisis. Dial 911 or proceed to emergency room.")
else:
     print("Invalid systolic and/or diastolic blood pressure entry.")

#the optimal and elevated conditions work but Stage 1, Stage 2, and Crisis don't. Still working on it. **Update: got it working**
print()
print("For more educational information on blood pressure, visit", "https://www.cdc.gov/bloodpressure/index.htm")

print()
#BG = blood glucose(sugar)

if int(blood_sugar) <= 75:
     print("Your glucose measurement of", blood_sugar, "is low. Contact your physician.")
elif int(blood_sugar) >= 76 and int(blood_sugar) <= 100:
     print("An 8hr fasted glucose measurement of", blood_sugar, "is normal.")
elif int(blood_sugar) >= 101 and int(blood_sugar) <= 140:
     print("A non-fasted glucose measurement of", blood_sugar, "is normal.")
elif int(blood_sugar) >= 141:
     print("Your glucose measurement of", blood_sugar, "is high. Contact your physician.")
else:
     print("Invalid blood glucose entry.")

print()
print("For more educational information on blood sugar, visit", "https://www.cdc.gov/diabetes/home/index.html")

print()
#ex_time = minutes of daily exercise

if int(ex_time) <= 149/7:
     print("Your daily exercise time of", ex_time, "is less than recommended. Consider increasing it to achieve 150-300 minutes per week to improve your health.")
elif int(ex_time) >= 150/7 and int(ex_time) <= 300/7:
     print("Your daily exercise time of", ex_time, "is within the recommended amount. Achieving 150-300 minutes per week will continue to improve your health.")
elif int(ex_time) >= 301/7:
     print("Your daily exercise time of", ex_time, "exceeds the recommended amount. Your weekly total should benefit your health.")
else:
     print("Invalid entry for minutes of daily exercise")

print()
print("For more educational information on recommended daily exercise for adults, visit", "https://health.gov/paguidelines/second-edition/pdf/Physical_Activity_Guidelines_2nd_edition.pdf#page=55")

print()
#steps = number of daily steps

if int(steps) <= 2999:
     print("Your total daily number of", steps, "steps is below average. Consider increasing it to improve your health.")
elif int(steps) >= 3000 and int(steps) <= 4000:
     print("Your total daily number of", steps, "steps is within the average. Consider continuing to increase the total to improve your health.")
elif int(steps) >= 4001 and int(steps) <= 10000:
     print("Your total daily number of", steps, "steps is above the average. Consider continuing to increase the total to improve your health.")
elif int(steps) >= 10001:
     print("Your total daily number of", steps, "steps exceeds the average recommended goal of 10,000. Your achievement shows commitment to your health.")
else:
     print("Invalid entry for number of daily steps.")

print()
print("For more educational information on recommended daily steps, visit", "https://www.cdc.gov/diabetes/prevention/pdf/postcurriculum_session8.pdf")

print()
#day_md = number of days since last MD appointment

if int(day_md) <= 180:
     print("It has been", day_md, "days since your last physician appointment. Check if another appointment is necessary.")
elif int(day_md) >= 181 and int(day_md) <= 364:
     print("It has been", day_md, "days since your last physician appointment. You may be overdue for a follow-up appointment.")
elif int(day_md) >= 364:
     print("It has been", day_md, "days since your last physician appointment. It is recommended to have a check-up at least once a year. Schedule an appointment to see your physician.")
else:
     print("Invalid entry for number of days since last MD appointment.")

print()
print("For more educational information on MD check-ups, visit", "https://www.cdc.gov/family/checkup/index.htm")
