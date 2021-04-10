#Program takes persons height & weight in centimeters & kilograms
# Stores height and weight in variables Weight and Height
# Third Variable(float) is calculated using inputted weight and height with BMI forumula

Height = float(input('Enter your heightin centimeters'))
Weight = float(input("Enter your weight in kilograms"))

BMI = str((Weight/(Height**2)*10000))

print("Your BMI is : " + BMI)