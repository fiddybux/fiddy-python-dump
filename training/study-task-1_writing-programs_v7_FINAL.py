#region Main "Title"
# coding=utf-8
"""Study Task 1(a), 1(b) and 1(c): Writing Programs
Author: Russell Dyson
Custom region folding: "Visual Studio Code Custom Folding Extension" (maptz)
"""
#endregion
#region Main "Setup Environment"
import os
import time
os.system('cls')
class formatting:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
#endregion

# Task (a) - Time Converter
#region Main "Docstring"

"""(a) Write a program that includes a function that returns the total number of
seconds, calculated from a whole number of hours, minutes and seconds provided
as 3 parameters.
"""
#endregion
#region Main "Time Converter"
def timeConvert():
    print(
        formatting.BOLD + formatting.UNDERLINE + 
        "Time Converter" + formatting.END
        )
    print(
        formatting.PURPLE + "\nThis programme will convert " 
        + formatting.END 
        + formatting.RED + "hours " + formatting.END 
        + formatting.PURPLE + ", " + formatting.END 
        + formatting.BLUE + "minutes " + formatting.END 
        + formatting.PURPLE + "and " + formatting.END
        + formatting.YELLOW + "seconds " + formatting.END 
        + formatting.PURPLE + "into " + formatting.END
        + formatting.DARKCYAN + formatting.UNDERLINE + "SECONDS" 
        + formatting.END
        )
    print(
        formatting.PURPLE + 
        "\nPlease enter the hours, minutes and seconds...\n" 
        + formatting.END
        )
    hrsInput = input("Enter hours: ")
    minInput = input("Enter minutes: ")
    secInput = input("Enter seconds: ")
    hrsToSec = int(hrsInput) * 3600
    minToSec = int(minInput) * 60 
    secToSec = int(secInput)
    secOutput = int(hrsToSec + minToSec + secToSec)
    print(
        "\n>>>",
        formatting.RED + str(hrsInput) + formatting.END,"hours,",
        formatting.BLUE + str(minInput) + formatting.END,"minutes and",
        formatting.YELLOW + str(secInput) + formatting.END,"seconds",
        formatting.UNDERLINE + "equals" + formatting.END,
        formatting.BOLD + formatting.GREEN + str(secOutput) + formatting.END,
        "seconds.\n"
        )
#endregion

# Task (b) - Measurement Converter
#region Main "Docstring"
"""(b) Write a program to convert measurements between feet and inches and metres
and centimetres. The program should ask the user whether they wish to convert
from metres and centimetres to feet and inches, or from feet and inches to
metres and centimetres. Create two functions (one for conversion one way, and
the other for conversion the other way) and each should take two parameters (the
number of feet and inches (one parameter for each) or the number of metres and
centimetres (one parameter for each).

The conversions are:
1 inch = 2.54 cm		1 foot = 30.48 cm
1 cm =   0.397 inches	1 metre = 39.37 inches
"""
#endregion
#region Main "Measurement Converter"
def conversionQuestion():
    print(
        formatting.BOLD + formatting.UNDERLINE + 
        "Measurement Converter" + formatting.END
        )
    print(
        formatting.PURPLE + "\nThis programme will convert" + formatting.END, 
        formatting.CYAN + formatting.UNDERLINE + 
        "Metric to Imperial" + formatting.END,
        formatting.PURPLE + "and" + formatting.END,
        formatting.GREEN + formatting.UNDERLINE + 
        "Imperial to Metric" + formatting.END
        )
    print(
        formatting.PURPLE + 
        "\nPlease make a selection...\n" 
        + formatting.END
        )
    print(
        "Type", formatting.CYAN + "1" + formatting.END, 
        "for" + formatting.CYAN,
        "Metric to Imperial" + formatting.END,
        "conversion."
        )
    print(
        "Type", formatting.GREEN + "2" + formatting.END,
        "for" + formatting.GREEN,
        "Imperial to Metric" + formatting.END,
        "conversion.\n"
        )
    conversionType = \
        int(input(
            "Enter your selection ('" + formatting.CYAN + 
            "1" + formatting.END + "' or '" + formatting.GREEN + 
            "2" + formatting.END + "'): ")
            )
    if conversionType == 1:
        print(
            "\nYou have selected" + formatting.CYAN,
            "Metric to Imperial" + formatting.END,
            "conversion."
            )
    elif conversionType == 2:
        print(
            "\nYou have selected" + formatting.GREEN,
            "Imperial to Metric" + formatting.END,
            "conversion."
            )
    loop = True
    while loop is True:
        if conversionType == 1:
            metresInput = input("\nEnter metres: ")
            centimetresInput = input("Enter centimetres: ")
            return metricToImperial(metresInput,centimetresInput)
        elif conversionType == 2:
            feetInput = input("\nEnter feet: ")
            inchesInput = input("Enter inches: ")
            return imperialToMetric(feetInput,inchesInput)
        else:
            print(
                formatting.RED + 
                "\nThat is not a valid selection!\n" + formatting.END
                )
            print(
                "Type", formatting.CYAN + 
                "1" + formatting.END,
                "for", formatting.CYAN + 
                "Metric To Imperial" + formatting.END
                )
            print(
                "Type", formatting.GREEN + 
                "2" + formatting.END,
                "for", formatting.GREEN + 
                "Imperial to Metric\n" + formatting.END
                )
            conversionType = \
                int(input(
                    "Enter your selection ('" + formatting.CYAN + 
                    "1" + formatting.END + "' or '" + formatting.GREEN + 
                    "2" + formatting.END + "'): ")
                    )
            if conversionType == 1:
                print(
                    "\nYou have selected" + formatting.CYAN,
                    "Metric to Imperial" + formatting.END,
                    "conversion."
                    )
            else:
                print(
                    "\nYou have selected" + formatting.GREEN,
                    "Imperial to Metric" + formatting.END,
                    "conversion."
                    )

def metricToImperial(metresInput,centimetresInput):
    metricConversionImperial = \
        ((float(metresInput)) * 39.37) + ((float(centimetresInput)) * 0.397)
    print(
        "\n" + metresInput,"metres and", centimetresInput,"centimetres into", 
        formatting.UNDERLINE + "inches" + 
        formatting.END + ":" + 
        formatting.BOLD + formatting.GREEN, 
        round(metricConversionImperial,2), formatting.END + "inches"       
        )
    inchesToFeet = metricConversionImperial * 0.0833333333333
    print(
        "In feet (ft) that is: ", 
        formatting.BLUE + str(round(inchesToFeet,2)) + formatting.END,
        "ft\n"
        )

def imperialToMetric(feetInput,inchesInput):
    imperialConversionMetric = \
        ((float(feetInput)) * 30.48) + ((float(inchesInput)) * 2.54)
    print(
        "\n" + feetInput,"feet and", inchesInput,"inches into", 
        formatting.UNDERLINE + "centimetres" + 
        formatting.END + ":" + 
        formatting.BOLD + formatting.GREEN, 
        round(imperialConversionMetric,2), formatting.END + "centimetres"
        )
    centimetersToMetres = imperialConversionMetric * 0.01
    print(
        "In metres (m) that is: ", 
        formatting.BLUE + str(round(centimetersToMetres,2)) + formatting.END, 
        "m\n"
        )
#endregion

# Task (c) - Pay Calculator
#region Main "Docstring"
"""(c) Write a program to calculate an employee’s pay. It should ask the user to
input the number of hours worked in the week (maximum 60 hours), and the rate
per hour. For each hour over 40 hours worked, it should calculate overtime pay
at 1.5 times the basic hourly rate. In the program include functions for getting
the user input, calculating basic pay and overtime pay, and for outputting the
result.
"""
#endregion
#region Main "Pay Calculator"
def payCalcInput():
    print(
        formatting.BOLD + formatting.UNDERLINE + 
        "Pay Calculator" + formatting.END
        )
    print(
        formatting.PURPLE + 
        "\nThis programme will calculate normal pay (40 hour cap) based on",
        "user-inputted pay rate, and calculate overtime pay (60 hour cap)",
        "at 1.5 times normal pay rate." + formatting.END
        )   
    hoursWorked = \
        float(
            input(formatting.YELLOW + 
            "\nEnter the number of hours worked this week " + \
            "(e.g. '16.5'): " + formatting.END)
            )
    while True:
        if hoursWorked > 0 and hoursWorked <= 60:
            if hoursWorked <= 40:
                hoursWorkedNorm = hoursWorked
                ratePerHourNorm = float(
                    input(
                        formatting.CYAN + 
                        "\nEnter your rate of pay per hour (££.pp): " +
                        formatting.END)
                    )
                print(
                    "\nYou worked a total of",
                    str(round(hoursWorkedNorm)),"hours normal time"
                    )
                print(
                    "Pay is being calculated at £{:.2f}" \
                        .format(ratePerHourNorm),"per hour (<= 40 hours)\n")
            else:
                hoursWorkedNorm = int(40)
                hoursWorkedOver = int(hoursWorked - 40)
                # print(hoursWorkedNorm,hoursWorkedOver) # PRINTING THE RATES
                ratePerHourNorm = float(
                    input(
                        formatting.CYAN + 
                        "\nEnter your rate of pay per hour (££.pp): " +
                        formatting.END)
                    )
                ratePerHourOver = float(ratePerHourNorm * 1.5)
                print(
                    "\nYou worked a total of",
                    str(round(hoursWorkedNorm)),"hours normal time, and",
                    str(round(hoursWorkedOver)), "hours overtime"
                    )
                print(
                    "\nPay is being calculated at £{:.2f}" \
                        .format(ratePerHourNorm),
                        "per hour (<= 40 hours)"
                        )
                print(
                    "Pay is being calculated at £{:.2f}" \
                        .format(ratePerHourOver),
                        "per hour (> 40 to 60 hour range)\n"
                        )
                return payCalcOver(
                    hoursWorkedNorm,ratePerHourNorm,
                    hoursWorkedOver,ratePerHourOver
                    )
            return payCalcNorm(
                hoursWorkedNorm,ratePerHourNorm
                )
        else:
            print(
                formatting.BOLD + 
                "\nYou can't work less than 0 hours or more than 60 hours!" +
                formatting.END)
            print(formatting.RED + "Please try again." + formatting.END + "\n")
            hoursWorked = \
                float(
                    input(formatting.YELLOW + 
                    "Enter the number of hours worked this week " + \
                    "(e.g. '16.5'): " + formatting.END)
                    )

def payCalcNorm(
    hoursWorkedNorm,ratePerHourNorm
    ):
    msg = (
        formatting.PURPLE + 
        "Calculating NORMAL pay only..." + 
        formatting.END
        )
    for i in range(3): 
        print(msg)
        time.sleep(0.25)
    payCalc = hoursWorkedNorm * ratePerHourNorm
    return payCalcOutput(payCalc)

def payCalcOver(
    hoursWorkedNorm,ratePerHourNorm,
    hoursWorkedOver,ratePerHourOver
    ):
    msg = (
        formatting.PURPLE + 
        "Calculating NORMAL pay and OVERTIME pay..." + 
        formatting.END
        )
    for i in range(3): 
        print(msg)
        time.sleep(0.25)
    payCalc = \
        (hoursWorkedNorm * ratePerHourNorm) \
        + (hoursWorkedOver * ratePerHourOver)
    return payCalcOutput(payCalc)

def payCalcOutput(payCalc):
    print (
        "\nYour pay is:",
        formatting.UNDERLINE + formatting.GREEN + 
        "£{:.2f}\n".format(payCalc) + formatting.END
        )
#endregion

# Call all functions from within main()
#region Main
def main():
    timeConvert()
    conversionQuestion()
    payCalcInput()
#endregion

# Call main() function
main()