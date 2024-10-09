#2. The Greatest Showdown
#Task 1: Identify the Greatest \ 
# Write a Python program that asks the user to enter three numbers.\
# Your code should then identify and print out the largest number among the three.

num_1 =input("enter first number:") 
num_2 =input("enter second number:")
num_3 =input("enter third number:")

if (num_1 > num_2) and (num_1 > num_3):
        print(num_1 + " is the largest  number!")
elif (num_2 > num_1) and (num_2 > num_3):
    print(num_2 + " is the largetst number!")
else:
    print(num_3 + " is the largest number!")