import Person

def main():
    print("Main running")
    print("Test global variable in module: " + str(Person.pi)) 
    print("Test function in module: " + str(Person.plusOne))
    print("Initialize a class: ")
    p = Person.Person("John", 36)
    print(p.name)
    print(p.age)
    p.setAge(40)
    print("Use method to set value:" + str(p.age))

  
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()
