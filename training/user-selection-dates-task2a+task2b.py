# Task 1.1: Programming User Selection
import time

# Month number to alphanumberic month function
def MonthNum():
    month_num = int(input("Enter a whole number between 1 and 12: "))
    if month_num == int(1):
        print("January")
    elif month_num == int(2):
        print("February")
    elif month_num == int(3):
        print("March")
    elif month_num == int(4):
        print("April")
    elif month_num == int(5):
        print("May")
    elif month_num == int(6):
        print("June")
    elif month_num == int(7):
        print("July")
    elif month_num == int(8):
        print("August")
    elif month_num == int(9):
        print("September")
    elif month_num == int(10):
        print("October")
    elif month_num == int(11):
        print("November")
    elif month_num == int(12):
        print("December")
    else:
        print("That number is not a number between 1 and 12")
MonthNum()
time.sleep(1)

# Task 1.2: Programming User Selection
# Enter numbers (not validated) to construct date in format 'nnth Month YYYY'
def ConstructDate():
    num_day = int(input("Enter a whole number for day of the month: "))
    num_month = int(input("Enter a whole number for month of the year: "))
    num_year = int(input("Enter a whole number for year of the century: "))
    if num_month == int(1):
        alpha_month = str("January")
    elif num_month == int(2):
        alpha_month = str("February")
    elif num_month == int(3):
        alpha_month = str("March")
    elif num_month == int(4):
        alpha_month = str("April")
    elif num_month == int(5):
        alpha_month = str("May")
    elif num_month == int(6):
        alpha_month = str("June")
    elif num_month == int(7):
        alpha_month = str("July")
    elif num_month == int(8):
        alpha_month = str("August")
    elif num_month == int(9):
        alpha_month = str("September")
    elif num_month == int(10):
        alpha_month = str("October")
    elif num_month == int(11):
        alpha_month = str("November")
    elif num_month == int(12):
        alpha_month = str("December")
    else:
        pass
    print("The date you entered is", num_day,"st/nd/rd/th", alpha_month, num_year)
ConstructDate()
time.sleep(1)
