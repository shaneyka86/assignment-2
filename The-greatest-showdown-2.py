#Task 2: Identify the Smallest Improve upon your code from \
#Task 1 to also determine the smallest number among the three and 
# print it out.
#Expected Outcome: If we provide the numbers 3, 3, and 4,
# it should print out that "The smallest number is 3. 
# The largest number is 4. 

num_1 =input("enter first number:") 
num_2 =input("enter second number:")
num_3 =input("enter thrid number:")

if (num_1 < num_2) and (num_1 < num_3):
    print(num_1 + " is the smallest  number!")
elif (num_2 < num_1) and (num_2 < num_3):
    print(num_2 + " is the smallest number!")
else:
    print(num_2 + " is the smallest number")
    