# 4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
# Do not name your variable sum or use the sum() function.

def computepay():
    try:
        hrs = input("Enter Hours:")
        h = float(hrs)
    except:
        print("Error, please enter number.")
        quit()
    try:
        pr = input("Enter Pay Rate:")
        r = float(pr)
    except:
        print("Error, please enter number.")
        quit()
    global p
    #https://www.geeksforgeeks.org/global-local-variables-python/
    if h > 40:
        reg = 40 * r
        opt = (h-40) * (r*1.5)
        p = reg + opt
    else:
        p = h * r
    return p

    # print("Pay", p)
    # Note! This line will not execute since it is after return
    # https://python.plainenglish.io/executing-code-after-a-return-statement-in-python-functions-887dba33004d

computepay()
print("Pay:", p)

#See global, local reference:
#https://www.geeksforgeeks.org/global-local-variables-python/

# Assignment practice answer
# def computepay(h, r):
#     if h > 40:
#         reg = 40 * r
#         opt = (h-40) * (r*1.5)
#         p = reg + opt
#     else:
#         p = h * r
#     return p
#
# hrs = float(input("Enter Hours:"))
# pr = float(input("Enter Pay Rate:"))
# p = computepay(hrs, pr)
# print("Pay", p)
