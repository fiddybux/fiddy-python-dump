# Task 1.3: Programming User Selection
# Validated Date Program
import time
import sys
def ValidDate():

    # Year section
    year_num = int(input("Enter the year number (> 0): "))
    if year_num <= int(0):
        print("Year number must be above 0!")
        time.sleep(1)
        input("Press ENTER to exit!")
        sys.exit()
    else:
        pass

    # Month section
    num_month_input = int(input
        ("Enter a whole number for day of the month (1 - 12): "))
    if num_month_input == int(1):
        alpha_month_out = str("January")
    elif num_month_input == int(2):
        alpha_month_out = str("February")
    elif num_month_input == int(3):
        alpha_month_out = str("March")
    elif num_month_input == int(4):
        alpha_month_out = str("April")
    elif num_month_input == int(5):
        alpha_month_out = str("May")
    elif num_month_input == int(6):
        alpha_month_out = str("June")
    elif num_month_input == int(7):
        alpha_month_out = str("July")
    elif num_month_input == int(8):
        alpha_month_out = str("August")
    elif num_month_input == int(9):
        alpha_month_out = str("September")
    elif num_month_input == int(10):
        alpha_month_out = str("October")
    elif num_month_input == int(11):
        alpha_month_out = str("November")
    elif num_month_input == int(12):
        alpha_month_out = str("December")
    else:
        print("Month number must be between 1 and 12!")
        time.sleep(1)
        input("Press ENTER to exit!")
        sys.exit()

    # Day section + validation
    num_day_input = str(input("Enter day number (1 - 31): "))
    if num_day_input == str("0") or num_day_input >= str("32"):
        print("Day number must be between 1 and 31!")
        time.sleep(1)
        exit()
    elif num_day_input == str("1") or num_day_input == str("21") or num_day_input == str("31"):
        day_date = num_day_input + "st"
    elif num_day_input == str("2") or num_day_input == str("22"):
        day_date = num_day_input + "nd"
    elif num_day_input == str("3") or num_day_input == str("23"):
        day_date = num_day_input + "rd"
    else:
        day_date = num_day_input + "th"

    # Month validation
    if alpha_month_out == "February" and int(num_day_input) <= int(28):
        valid_date = True
    elif alpha_month_out == "April" or alpha_month_out == "June" or alpha_month_out == "September" and int(num_day_input) <= int(30):
        valid_date = True
    elif alpha_month_out in ["January","March","May","July","August","October","December"] and int(num_day_input) <= int(31):
        valid_date = True
    else:
        valid_date = False

    # Output section
    if valid_date:
        print(day_date, alpha_month_out, year_num)
    else:
        print("Not valid date!")
        time.sleep(1)
        input("Press ENTER to exit!")
        sys.exit()
        
ValidDate()
time.sleep(1)
