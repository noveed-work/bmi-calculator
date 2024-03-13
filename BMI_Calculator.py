#BMI Calculator v2
#BMI is calculated by dividing the weight with the height squared

print("Welcome to the BMI calculator")
name = input("What is your name?\n")
print(f"Hi {name} Lets check what your BMI is")
height = float(input("What is your height in meters?\n"))
weight = int(input("What is your weight in KG's?\n"))
height = (height ** 2)
bmi = float(weight / height)
bmi = round(bmi, 2)
if bmi<=18.5:
  print(f"Your BMI is {bmi} and you are classed as underweight")
elif bmi<=24.9:
  print(f"Your BMI is {bmi} and you are classed as normal")
elif bmi<=29.9:
  print(f"Your BMI is {bmi} and you are classed as Overweight")
elif bmi<=34.9:
  print(f"Your BMI is {bmi} and you are classed as Obese")
elif bmi>34:
  print(f"Your BMI is {bmi} and you are classed as Extrmeley Overweight")