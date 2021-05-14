# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round (weight / height ** 2,1)
if BMI < 18.5:
  result = "You are underweight."
elif BMI < 25:
  result = "You have a normal weight."
elif BMI < 30:
  result = "You are slightly overweight."
elif BMI < 35:
  result = "You are obese."
else:
  result = "You are clinically obese."
print (f" Your BMI is {BMI}, {result}")

