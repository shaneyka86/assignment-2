#Task 1: Leap Year Checker Write a Python program that prompts the user to input a year. 
# The program should determine if the given year is a leap year or not and
# then display an appropriate message. 
#Please note that this is the definition of a leap year:
# Every year that is exactly divisible by four is a leap year, 
# except for years that are exactly divisible by 100, 
# but these centurial years are leap years if they are exactly divisible by 400.

leap_year=int(input("Enter a year:"))
if (leap_year%4==0) and (leap_year%100!=0):
    print("The year is a leap year")
elif leap_year %400==0:
    print("The year is a leap year")
else:   
    print("The year is not a leap year")
    