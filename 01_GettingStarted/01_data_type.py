
import sys


print("Please enter case you want to test: ")
print(sys.argv)

if sys.argv[1] == 1:
    num_int = 123
    num_flo = 1.23 

    num_new = num_int + num_flo

    print("datatype of num_int:", type(num_int))
    print("size for datatype of num_int:", sys.getsizeof(num_int))

    print("datatype of num_flo:", type(num_flo))
    print("size for datatype of num_flo:", sys.getsizeof(num_int))

    print("Value of num_new:",num_new)
    print("datatype of num_new:", type(num_new))

else :
    num_int = 123
    num_str = "456"
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    print("Data type of num_int:",type(num_int))
    print("size for datatype of num_int:", sys.getsizeof(num_int))

    print("Data type of num_str:",type(num_str))
    print("size for datatype of num_str:", sys.getsizeof(num_str))

    print("Data type of thisdict:",type(thisdict))
    print("size for datatype of thisdict:", sys.getsizeof(thisdict))


    # print(num_int+num_str)
