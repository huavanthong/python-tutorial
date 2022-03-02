# Lambda is an anonymous function in Python, that can accept any number of arguments, but can only have a single expression. 
# It is generally used in situations requiring an anonymous function for a short time period. 
# Lambda functions can be used in either of the two ways:
# *     Assigning lambda functions to a variable.
# *     Wrapping lambda functions inside another function.

# Refer: https://stackoverflow.com/questions/890128/how-are-lambdas-useful

import time

# Python3 code to demonstrate
# to generate random number list
# using list comprehension + randrange()
import random

def main():

    print("Please select case do you want to learn: ")
    print("Case 1: Assigning lambda functions to a variable.")
    print("Case 2: Wrapping lambda functions inside another function.")
    print("Case 3: Use lamdata to implement a filter.")
    print("Case 4: Sorting by an alternate key")

    # Because input from user, it is string format, so we need to convert integer type.
    val = int(input("Enter your case: "))

    if 1 == val:
        print("Step 1: to understand about lamda, firstly, you need to ask yourself? What exactly do you want?")
        time.sleep(1)
        print("You want: create a function which multiply by each other ")
        time.sleep(1)
        print("Step 2: to start this idea, we need 2 argument parameter ===> We can use lamda")
        mul = lambda a, b : a * b
        print(mul(2, 5))    # output => 10
    elif 2 == val:
        mulFive = myWrapper(5)
        print(mulFive(2))    # output => 10
    elif 3 == val: 
        print("Step 1: you will implement a lamda to get multiples of 3.")
        time.sleep(0.5)
        mult3 = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        print(mult3)
        
        print("Now, we have a method to convert filter to list")
        print(list(mult3))

        print("Step 2: try to compare with customerize function, implement filterfunc().")
        time.sleep(0.5)
        mult3 = filter(filterfunc, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        print(mult3)

        print("Now, we have a method to convert filter to list")
        print(list(mult3))

        print("Result: it are the same result")
        time.sleep(0.5)
        print("Conclusion: Lamdata is a anonymous function exist in a short time, it instead of a customize filterfunc()")

    elif 4 == val:
        print("Start this case, we need input a serial number from 1->9")
        time.sleep(0.5)
        print("Step 1: Now, we create a list from 1->9 with random vale ")
        arr = [random.randrange(1, 10, 1) for i in range(10)]
        print("     A list with random value: " + str(arr))

        print("Step 2: we will sort by order")
        arr = sorted(arr)
        print("     A list after sorted: " + str(arr))
        print("If you want sort ")

        print("Step 3: we will sort it by lamda x: abs(5-x)")
        sorted(arr, key=lambda x: abs(5-x))
        print("     Final output: " + str(arr))
    else: 
            print("Invalid case !!!")

def filterfunc(x):
    return x % 3 == 0

def myWrapper(n):
    return lambda a : a * n
    

# Using the special variable 
# __name__
if __name__=="__main__":
    main()
