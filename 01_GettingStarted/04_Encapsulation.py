####################################################################################################################################################
# 1. Encapsulation using through protected member and private member.

####################################################################################################################################################
#################################################################
# Python program to
# demonstrate protected members
#################################################################

# Creating a base class
class Base:
    def __init__(self):
         
        # Protected member
        self._a = 2     ## Dash sign is show that this is the protected member.
 
# Creating a derived class   
class Derived(Base):
    def __init__(self):
         
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ")
        print(self._a)
 
obj1 = Derived()
         
obj2 = Base()
 
# Calling protected member
# Outside class will  result in
# AttributeError
print(obj2.a)

#################################################################
# Python program to
# demonstrate private members
#################################################################

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks" ## Double dash sign is show that this is the protected member.
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
         
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
# Driver code
obj1 = Base()
print(obj1.a)
 
# Uncommenting print(obj1.c) will
# raise an AttributeError
 
# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class