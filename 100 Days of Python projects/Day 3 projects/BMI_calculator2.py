height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

a = float(height)
b = int(weight)

BMI = (b / (a **2))
bmi_as_int = int(BMI)

if bmi_as_int < 18.5:
  print("You are underweight")
elif bmi_as_int < 25:
  print("You have normal weight")
elif bmi_as_int < 30:
  print("You are slightly overweight")
elif bmi_as_int < 35:
 print("You are obsese")
else:
 print("You are very obese")