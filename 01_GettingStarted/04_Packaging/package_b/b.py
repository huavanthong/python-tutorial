
import sys


def main_function_b():
    num_int = 123
    num_flo = 1.23 

    num_new = num_int + num_flo

    print("datatype of num_int:", type(num_int))
    print("size for datatype of num_int:", sys.getsizeof(num_int))

    print("datatype of num_flo:", type(num_flo))
    print("size for datatype of num_flo:", sys.getsizeof(num_int))

    print("Value of num_new:",num_new)
    print("datatype of num_new:", type(num_new))
