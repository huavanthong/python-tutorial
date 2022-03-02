
# Refer: https://codeblessu.com/python/size-of-data-types.html#Memory-requirement-for-List

import time
from termcolor import colored
import sys

def main():

    print(''' 
    
    This tutorial help you understand about size of data-type in Python.

    ''')
    time.sleep(2)

    while True:
        print(''' 

    Please select case do you want to learn: 
        Case 1: Size of Boolean.
        Case 2: Size of Int/Float.
        Case 3: Memory requirement for List.
        Case 4: Memory requirement for Tuple.
        Case 5: 

        ''')
 
        val = int(input("Enter your case: "))

        if 1 == val: 
            print("Python boolean variable requires minimum 24 bytes on 32-bit / 64-bit system. It may vary as per hardware.")
            print("Size of bool(): " + str(sys.getsizeof(bool()))) # prints 24
            print("Size of True: " + str(sys.getsizeof(True))) # prints 28
            print("Size of False: " + str(sys.getsizeof(False))) # prints 24

        elif 2 == val: 
            print("Python " + colored('int variable requires minimum 24 bytes on 32-bit / 64-bit system.','yellow') + ". It may vary as per hardware.")
            print("Size of: " + str(sys.getsizeof(int()))) # prints 24
            print("Size of: " + str(sys.getsizeof(0))) # prints 24
            print("Size of: " + str(sys.getsizeof(1))) # prints 28
            print("Size of: " + str(sys.getsizeof(-2))) # prints 28
            print("Size of: " + str(sys.getsizeof(2* 10**307))) # prints 164

        elif 3 == val:
            print("Python " + colored('list requires minimum 64 bytes on 32-bit / 64-bit system','yellow') + ". It may vary as per hardware.")
            size_t = sys.getsizeof( list() ) # prints 64
            print(size_t)

            a = []
            size_t = sys.getsizeof( a ) # prints 64
            print(size_t)

            a = [1]
            size_t = sys.getsizeof( a ) # prints 72
            print(size_t)
            a = [1,1]
            size_t = sys.getsizeof( a ) # prints 80
            print(size_t)

            a = [1]*10 # assigns 10 elements i.e. [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            size_t = sys.getsizeof( a ) # prints 144
            print(size_t)
            print("Now, we let start to next step!")
            a = ["Hello, let this be long string occupying more and more and more bytes", 1.2]
            size_t = sys.getsizeof( a ) # prints 80
            print(size_t)
            size_t = sys.getsizeof( a[0] ) # Check, individual element is occupying more bytes than overall list.
            print(size_t)
            size_t = sys.getsizeof( a[1] ) # prints 24 for float
            print(size_t)
        elif 4 == val:

            print("Python " + colored('tuple requires minimum 48 bytes on 32-bit / 64-bit system','yellow') + ". It may vary as per hardware. Note: Tuple occupies less memory space compare to list.")
            print("Size of tuple(): " + str(sys.getsizeof(tuple()))) # prints 48
            a = ()
            print("Size of a = (): " + str(sys.getsizeof(a))) # prints 48

            a = (1,)
            print("Size of a = (1,): " + str(sys.getsizeof(a))) # prints 56

            a = (1,1)
            print("Size of a = (1,1): " + str(sys.getsizeof(a))) # prints 64

            a = (1,)*10 # assigns 10 elements i.e. (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
            sys.getsizeof( a ) # prints 128

            a = ("Hello, let this be long string occupying more and more and more bytes", 1.2)
            sys.getsizeof(a) # prints 64
            sys.getsizeof(a[0]) # Check, individual element is occupying more bytes than overall tuple.
            sys.getsizeof(a[1]) # prints 24 for float
            time.sleep(1)
            print("Conclusion: Size of list is greater size of tuple")
        else: 
            print("Invalid case!!")

        time.sleep(3)


if __name__=="__main__":
    main()
