
import time
from termcolor import colored

class ArrayList:
    # Init is a constructor for class.
    # Self is a argument like this in Java
    def __init__(self, number_list):
       self.numbers = number_list

    # Iter method => make this class become iterable
    # Normally, iter will initalize a index to loop itself.
    def __iter__(self):
       self.pos = 0
       return self
    # Next method => move to another object
    # Please refer how to handle a loop object in class.
    def __next__(self):
       if(self.pos < len(self.numbers)):
           self.pos += 1
           return self.numbers[self.pos - 1]
       else:
           raise StopIteration

def main():

    print("Please select case do you want to learn: ")
    print("Case 1: Initalize a iterators inside a class.")
    print("Case 2: Make a string object to iterators object.")
    print("Case 3: Iteralbe in list, tuple, dict.")

    val = int(input("Enter your case: "))
    if 1 == val: 
        print(''' 
        Here is an example of a class implements all properties for Iterators.s
        ''') 
        print("        Note: One of the keyword you need to remember it is " + colored('StopIteration','red')); 
        array_obj = ArrayList([1, 2, 3])
        it = iter(array_obj)
        print(next(it)) #output: 2
        print(next(it)) #output: 3
        print(next(it))

        print("If you are boring, you can use syntax "+colored('in','green')+" to loop inside")
        for i in it:
            print(i)

        print("Final: You can see, they has a same result")
        #Throws Exception
        #Traceback (most recent call last):
        #...
        #StopIteration
    elif 2 == val: 
        print(''' 
        
        Here is an example of a python inbuilt iterator
        value can be anything which can be iterate
        
        
        ''')
        time.sleep(1)

        iterable_value = 'Geeks'
        iterable_obj = iter(iterable_value)
        print("Step 1: Suppose that you have a string: " + colored(iterable_value, 'green'))

        print('''Step 2: If you want to print each character in your string, or loop to each character,
        You need to convert string object to iterators object.
        Note: Everything in Python are object
        ''')
        
        while True:
            try:
        
                # Iterate by calling next
                item = next(iterable_obj)
                print(item)
            except StopIteration:
        
                # exception will happen when iteration will over
                break
    elif 3 == val:
        print(''' 
        
            Lists, tuples, dictionaries, and sets are all iterable objects. 
            They are iterable containers which you can get an iterator from.

        ''')

        # Sample built-in iterators

        # Iterating over a list
        print("List Iteration")
        l = ["geeks", "for", "geeks"]
        for i in l:
            print(i)
            
        # Iterating over a tuple (immutable)
        print("\nTuple Iteration")
        t = ("geeks", "for", "geeks")
        for i in t:
            print(i)
            
        # Iterating over a String
        print("\nString Iteration")   
        s = "Geeks"
        for i in s :
            print(i)
            
        # Iterating over dictionary
        print("\nDictionary Iteration")  
        d = dict()
        d['xyz'] = 123
        d['abc'] = 345
        for i in d :
            print("%s  %d" %(i, d[i]))

    else: 
        print("Invalid case!!")

if __name__=="__main__":
    main()
