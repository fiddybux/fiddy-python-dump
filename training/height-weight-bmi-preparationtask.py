# Import time to add pauses in runtime, for usability
import time
print("This program will calculate your BMI based on inflexible user input!")
time.sleep(1)

# Calculate centimetres from inches
height_inch = float(input("Input your height in Inches: "))
height_cm = height_inch * 2.54
print("Your height in centimetres is: %.1f" % height_cm, "cm.") # %.1f specifies 1 decimal place
time.sleep (1)

# Calculate kilograms from pounds
weight_pounds = float(input("Input your weight in Pounds: "))
weight_kg = weight_pounds * 0.45
print("Your weight in Kilograms is: %.1f" % weight_kg, "kg.") # %.1f specifies 1 decimal place
time.sleep (1)

# Calcualte BMI
# BMI is the weight in kilograms divided by height in metres squared
height_metres = height_cm / 100
calc_bmi1 = weight_kg / (height_metres ** 2) # calcualtes metres squared manually
calc_bmi2 = weight_kg / pow (height_metres, 2) # calcualtes metres squared using pow function
print("Your BMI (**) is: %.2f" % calc_bmi1) # %.2f specifies 2 decimal places
time.sleep (1)
print("Your BMI (pow) is: %.4f" % calc_bmi2) # %.4f specifies 4 decimal places
time.sleep (2)

