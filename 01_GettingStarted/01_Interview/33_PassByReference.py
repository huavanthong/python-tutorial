# Refer: https://www.interviewbit.com/python-interview-questions/#how-are-arguments-passed-by-value-or-by-reference-in-python

def main():
    arr = [1, 2, 3]
    print(arr)
    appendNumber(arr)
    print(arr)  

# Pass by reference: Reference to the actual object is passed. 
# Changing the value of the new object will change the value of the original object.
def appendNumber(arr):
    arr.append(4)
    
# Using the special variable 
# __name__
if __name__=="__main__":
    main()
