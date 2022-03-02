


class Parent1(object):  
   # Constructor
   def __init__(self, name):
       self.name = name    
 
class Child1(Parent1): 
   # Constructor
   def __init__(self, name, age):
       Parent1.name = name
       self.age = age
 
   def display(self):
       print(Parent1.name, self.age)
 

class Parent2(object):
   # Constructor
   def __init__(self, name):
       self.name = name    
 
class Child2(Parent2):
   # Constructor
   def __init__(self, name, age):         
       ''' 
       In Python 3.x, we can also use super().__init__(name)
       ''' 
       super(Child2, self).__init__(name)
       self.age = age
 
   def display(self):
      # Note that Parent.name cant be used 
      # here since super() is used in the constructor
      print(self.name, self.age)
  
def main(): 

    print(''' 

    Please select case do you want to learn: 
        Case 1: Access parent members in the child class By using Parent class name.
        Case 2: Access parent members in the child class By using super()

        ''')

    val = int(input("Enter your case: "))
    
    if val == 1: 
        # Driver Code
        obj = Child1("Interviewbit", 6)
        obj.display()
    elif val == 2: 
        # Driver Code
        obj = Child2("Interviewbit", 6)
        obj.display()

    else : 
        print("Invalid case !!!")



# Using the special variable 
# __name__
if __name__=="__main__":
    main()
