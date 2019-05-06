
# #####################################################
# HMI 7540 - Healthcare Devlpm Section 1 Spring 2019  #
#                                                     #
# Emily Ennis                                         #
# Suzy Potter                                         #                    
# Nolan Taaca                                         #
#                                                     #
# Final Project                                       #
# May 6, 2019                                         #
# #####################################################


def getName():
    global name, first, last
    first = input("Enter your first (given) name: ")
    last = input("Ener your last (family) name: ")
    return first.capitalize() + " " + last.capitalize()
getName()
print()
print("Hi, " + first.title() , last.title() , ", let's get started.")


# Body Mass Index

def getBMI():
    global age, gender, height, weight, waist, BMI    
   
    age = input("Enter your AGE in years: ")
    gender = input("Enter your GENDER (Male/Female): ")
    height = input("Enter your HEIGHT in inches: ")
    weight = input("Enter your WEIGHT rounded to the nearest pound: ")
    waist  = input("Enter your WAIST CIRCUMFERENCE in inches: ") 
    
    BMI = int(float(weight)*float(703))/int((float(height)*float(height)))

    print("\nYour Body Mass Index is:", round(BMI,2))

    if BMI <= 18.4:
        print("BMI is your Body Mass Index. Your BMI is below normal range. Consult your physician.\n")
        print("For helpful weight management information, visit: ", "http://www.cdc.gov/healthyweight/effects/index.html")
    elif BMI >= 18.5 and BMI <= 24.9:
        print("BMI is your Body Mass Index. Your BMI is within normal range.")
    else:
        print("BMI is your Body Mass Index. Your BMI is above normal range. Consult your physician.\n")
        print("For helpful weight management information, visit: ", "http://www.cdc.gov/healthyweight/effects/index.html")

    #main()

    
#getBMI()    


# our Basal Metabolic Rate 

def getBMR():
    global BMR, calories

    if gender == "Female":
        BMR = 655 + int(4.35 * float(weight)) + int(4.7 * float(height)) - int(4.7 * float(age))
    else:
        BMR = 66 + int(6.23 * float(weight)) + int(12.7 * float(height)) - int(6.8 * float(age))

    calories = input("Enter total calorie intake for the day: ")

    print("You're reported calorie intake for the day is", calories + ".")
    print("Your Basal Metabolic Rate is:", BMR)

    main()


#getBMR()



# Body Fat Percentage

def getBFP():
    global BFP 
    
    print()
    print("For a healthy body-fat scale reference, visit: ", "\nhttps://www.acefitness.org/education-and-resources/lifestyle/tools-calculators/percent-body-fat-calculator")

    if gender == "female":
      
        BFP = str(float(1.20) * float(BMI) + float(0.23) * float(age) - float(5.4))
        print("You're estimated body fat percentage is",BFP[0:5])
    else:
        BFP = str(float(1.20) * float(BMI) + float(0.23) * float(age) - float(16.2))
        print("\nYou're estimated body fat percentage is",BFP[0:5])
        
    main()


#getBFP()


# Activity Level

def enterActivity(): 
    global activity_level
    
    print("""
    Activity Levels (2-Character Code)
    
    SD - Sedentary (little or no exercise)
    LA - Lightly Active (light exercise/sports 1-3 days/week)
    MA - Moderatetely Active (moderate exercise/sports 3-5 days/week)
    VA - Very Active (hard exercise/sports 6-7 days a week)
    EA - Extra Active (very hard exercise/sports & physical job or 2x training)
    """)
        
    activity_level = input("Review the options to select your activity_level: SD, LA, MA, VA, or EA: ")
    print()    
    if activity_level == "SD":
         TDC = int(float(BMR) * float(1.2))
         print("The daily total number of calories you need in order to maintain your current weight is", round(TDC,0))
    elif activity_level == "LA":
         TDC = int(float(BMR) * float(1.375))
         print("The daily total number of calories you need in order to maintain your current weight is", round(TDC,0))
    elif activity_level == "MA":
         TDC = int(float(BMR) * float(1.55))
         print("The daily total number of calories you need in order to maintain your current weight is", round(TDC,0))
    elif activity_level == "VA":
         TDC = int(float(BMR) * float(1.725))
         print("The daily total number of calories you need in order to maintain your current weight is", round(TDC,0))
    elif activity_level == "EA":
         TDC = int(float(BMR) * float(1.95))
         print("The daily total number of calories you need in order to maintain your current weight is", round(TDC,0))
    elif activity_level != "EA":
         print("Invalid entry. Please try again.")
            
    print("BMI is also BFP, estimated Body Fat Percentage",  "https://www.calculator.net/body-fat-calculator.html")
    
    print("\nThe daily total number of calories you need to lose about 1 pound per week is", int(float(TDC)-float(500)))
    print("The daily total number of calories you need to gain about 1 pound per week is", int(float(TDC)+float(500)))

    main()

#enterActivity() 


#WHR = Waist to Height Ratio

def getWHR():
    global WHR

    print()
    print("For more educational information on Waist-to-Height Ratio, visit", "\nhttp://prowellness.vmhost.psu.edu/families/understanding_risk/whtr")
    print()
        
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

    main()


#getWHR()


# Blood Pressure

def getBP():
    global SBP, DSP

    systolic_bp = input("Enter measured systolic blood pressure: ")
    diastolic_bp = input("Enter measured diastolic blood pressure: ")

    print("For more educational information on blood pressure, visit", "https://www.cdc.gov/bloodpressure/index.htm")
    print()
    
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

    main()

#getBP()


# Blood Glucose

def getBSugar():
    global blood_sugar
    
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
         print("Invalid blood glucose entry.")

    print()
    print("For more educational information on blood sugar, visit", "https://www.cdc.gov/diabetes/home/index.html")
    print()
    
    main()
    
#getBSugar()


# Minutes of Daily Exercise

def getExer():
    global ex_time
    
    ex_time = input("Enter daily exercise time in minutes: ")

    print("For more educational information on recommended daily exercise for adults, visit", "\nhttps://health.gov/paguidelines/second-edition/pdf/Physical_Activity_Guidelines_2nd_edition.pdf#page=55")
    print()
    
    if int(ex_time) <= 149/7:
         print("Your daily exercise time of", ex_time, "is less than recommended. Consider increasing it to achieve 150-300 minutes per week to improve your health.")
    elif int(ex_time) >= 150/7 and int(ex_time) <= 300/7:
         print("Your daily exercise time of", ex_time, "is within the recommended amount. Achieving 150-300 minutes per week will continue to improve your health.")
    elif int(ex_time) >= 301/7:
         print("Your daily exercise time of", ex_time, "exceeds the recommended amount. Your weekly total should benefit your health.")
    else:
         print("Invalid entry for minutes of daily exercise")

    main()
            
#getExer()


# Number of Daily Steps

def getSteps():
    global steps
    
    steps = input("Enter total steps for the day: ")

    print()
    print("For more educational information on recommended daily steps, visit", "\nhttps://www.cdc.gov/diabetes/prevention/pdf/postcurriculum_session8.pdf")
    print()
    
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

    main()

#getSteps()



# Number of days since last medical appointment

def getDoctor():
    global day_md
    
    day_md = input("Enter number of days since last MD appointment: ")
    
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
    print()

    main()
    
#getDoctor()


# MAIN QUERY

def main():   
    print("""
    Welcome to the Health Tracker

    [1] - Body Mass Index 
    [2] - Basal Metabolic Rate 
    [3] - Body Fat Percentage
    [4] - Activity Level
    [5] - Waist to Height Ratio
    [6] - Blood Pressure
    [7] - Glucose Measures
    [8] - Exercise Recommendations
    [9] - Step Recommendations
    [10]- Doctor Visits
    
    [E] - Exit
    """)

    while True:
        action = input('What would you like to review? (Enter an Option): ')

        if action == '1':
            print('1 selected')
            getBMI()
            main()
            break
        
        elif action == '2':
            print('2 selected')
            getBMI()
            getBMR()
            break
         
        elif action == '3':
            print('3 selected')
            getBMI()
            getBFP()
            break
         
        elif action == '4':
            print('4 selected')
            getBMI()
            getBMR()
            enterActivity()
            break
    
        elif action == '5':
            print('5 selected')
            getWHR()
            break

        elif action == '6':
            print('6 selected')
            getBP()
            break
        
        elif action == '7':
            print('7 selected')
            getBSugar()
            break

        elif action == '8':
            print('8 selected')
            getExer()
            break
        
        elif action == '9':
            print('9 selected')
            getSteps()
            break
         
        elif action == '10':
            print('10 selected')
            getDoctor()
            break
        
        elif action == 'E':
            print('\nExit selected')
            print("\nThank you, " + first + ". Enjoy your day.")  
            break
main() 
