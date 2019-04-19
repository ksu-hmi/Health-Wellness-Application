
#Add Users:
admins = {'Nolan':'taaca','Suzy':'potter','Emily':'ennis'}

# =============================================================================
# 
# ex_time = input("Enter daily exercise time in minutes: ")
# steps = input("Enter total steps for the day: ")
# calories = input("Enter total calorie intake for the day: ")
# protein = input("Enter total protein intake for the day in grams: ")
# carbs = input("Enter total carbohydrate intake for the day in grams: ")
# fat = input("Enter total fat intake for the day in grams: ")
# day_md = input("Enter number of days since last MD appointment: ")
# 
# =============================================================================


print()
#BMI=Body Mass Index Inputs

def enterBMI():    
    age = input("Enter your AGE in years: ")
    gender = input("Enter your GENDER (Male/Female): ")
    height = input("Enter your HEIGHT in inches: ")
    weight = input("Enter your WEIGHT rounded to the nearest pound: ")
    waist  = input("Enter your WAIST CIRCUMFERENCE in inches: ")
    
    BMI = str(int(float(weight)/float(2.205))/int((float(height)*float(0.0254))*(float(height)*float(0.0254))))
    print("Your BMI is: ", BMI[0:4])
    print()
    
    if BMI <= str(18.4):
         print("You're BMI is below normal range. Consult your physician.\n")
         print("For helpful weight management information, visit: ", "http://www.cdc.gov/healthyweight/effects/index.html")
    elif BMI >= str(18.5) and BMI <= str(24.9):
         print("You're BMI is within normal range.")
    else:
         print("You're BMI is above normal range. Consult your physician.\n")
         print("For helpful weight management information, visit: ", "http://www.cdc.gov/healthyweight/effects/index.html")
         
    enterBMR(age, gender, height, weight, waist, BMI)
    enterBFP(age, gender, BMI)
    
#BMR=Basal Metabolic Rate

def enterBMR(age, gender, height, weight, waist, BMI):
        
    calories = input("Enter your estimated DAILY CALORIE INTAKE: ")

    if gender == "female":
         BMR = str(655 + int(4.35 * float(weight)) + int(4.7 * float(height)) - int(4.7 * float(age)))
         print("Your BMR is: ", BMR)
    else:
         BMR = str(66 + int(6.23 * float(weight)) + int(12.7 * float(height)) - int(6.8 * float(age)))
         print("Your BMR is: ", BMR)
    enterActivity(BMR)

    print("You're reported calorie intake for the day is", calories)

print()    
#TDC=Total Daily Calories to maintain weight based on Harris Benedict Equation

def enterActivity(BMR):   
    print()
    print("Activity Levels")
    print("SD = Sedentary (little or no exercise)")
    print("LA = Lightly Active (light exercise/sports 1-3 days/week")
    print("MA = Moderatetely Active (moderate exercise/sports 3-5 days/week")
    print("VA = Very Active (hard exercise/sports 6-7 days a week")
    print("EA = Extra Active (very hard exercise/sports & physical job or 2x training")
    print()
    
    activity_level = input("Enter activity level: SD, LA, MA, VA, or EA: ")
        
    if activity_level == "SD":
         TDC = str(float(BMR) * float(1.2))
         print("The daily total number of calories you need in order to maintain your current weight is", TDC)
    elif activity_level == "LA":
         TDC = str(float(BMR) * float(1.375))
         print("The daily total number of calories you need in order to maintain your current weight is", TDC)
    elif activity_level == "MA":
         TDC = str(float(BMR) * float(1.55))
         print("The daily total number of calories you need in order to maintain your current weight is", TDC)
    elif activity_level == "VA":
         TDC = str(float(BMR) * float(1.725))
         print("The daily total number of calories you need in order to maintain your current weight is", TDC)
    elif activity_level == "EA":
         TDC = str(float(BMR) * float(1.95))
         print("The daily total number of calories you need in order to maintain your current weight is", TDC)
    else:
         print("Invalid entry.")
    
    print()
    print("The daily total number of calories you need to lose about 1 pound per week is", str(float(TDC)-float(500.0)))
    
    print()
    print("The daily total number of calories you need to gain about 1 pound per week is", str(float(TDC)+float(500.0)))
    
print()
#BFP = BMI estimated Body Fat Percentage (https://www.calculator.net/body-fat-calculator.html)

def enterBFP(age, gender, BMI):
    
    if gender == "female":
        BFP = str(float(1.20) * float(BMI) + float(0.23) * float(age) - float(5.4))
        print("You're estimated body fat percentage is",BFP[0:5])
    else:
        BFP = str(float(1.20) * float(BMI) + float(0.23) * float(age) - float(16.2))
        print("You're estimated body fat percentage is",BFP[0:5])

print()
#SBP = systolic blood pressure
#DSP = diastolic blood pressure

def enterBP():
    systolic_bp = input("Enter measured systolic blood pressure: ")
    diastolic_bp = input("Enter measured diastolic blood pressure: ")
    
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
         pass
    
    #the optimal and elevated conditions work but Stage 1, Stage 2, and Crisis don't. Still working on it. **Update: got it working**
    print()
    print("For more educational information on blood pressure, visit", "https://www.cdc.gov/bloodpressure/index.htm")

print()
#BG = blood glucose(sugar)

def enterBG():
    blood_sugar = input("Enter measured blood glucose: ")

    if int(blood_sugar) <= 75:
         print("Your glucose measurement of", blood_sugar, "is low. Contact your physician.")
    elif int(blood_sugar) >= 76 and int(blood_sugar) <= 100:
         print("An 8hr fasted glucose measurement of", blood_sugar, "is normal.")
    elif int(blood_sugar) >= 101 and int(blood_sugar) <= 140:
         print("A non-fasted glucose measurement of", blood_sugar, "is normal.")
    elif int(blood_sugar) >= 141:
         print("Your glucose measurement of", blood_sugar, "is high. Contact your physician.")
    else:
         pass
    
    print()
    print("For more educational information on blood sugar, visit", "https://www.cdc.gov/diabetes/home/index.html")

print()
def main():
    print("User: " + login)
    print("""
    Welcome to the Health Tracker

    [1] - Enter/Update BMI, BMR, and BG
    [2] - Enter/Update Calorie Intake
    [3] - Enter/Update Blood Pressure
    [4] - Enter/Update Exercise Info
    [5] - Enter/Update Glucose Measures
    [E] - Exit
    """)

    action = input('What would you like to do? (Enter a number) ')

    if action == '1':
        #print('1 selected')
        enterBMI()
        enterBMR()
        enterBFP()
    elif action == '2':
        #print('2 selected')
        enterActivity()
    elif action == '3':
        #print('2 selected')
        enterBP()
    elif action == '4':
        #print('3 selected')
        enterExercise()
    elif action == '5':
        #print('4 selected')
        enterGlucose()
    elif action == 'E':
        #print('Exit selected')
        exit()
    else:
        print('Please enter a valid option:') #need to cause it to reprompt

login = input('User: ')
password = input('Password: ')

if login in admins:
    if admins[login] == password:
        print('Welcome,',login)
        #now run the code
        while True:
            main()
    else:
        print('Invalid password.')
else:
    print('Invalid user.')
