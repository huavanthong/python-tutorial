# Refer: https://www.tutorialsteacher.com/python/property-decorator


class Student:
    def __init__(self, name):
        self.__name=name

    @property
    def name(self):
        return self.__name
    
    # @{property-name}.setter
    @name.setter   #property-name.setter decorator
    def name(self, value):
        self.__name = value
    
    # @{property-name}.deleter
    @name.deleter   #property-name.deleter decorator
    def name(self):
        print('Deleting..')
        del self.__name


def main():
    s = Student('Steve')
    print(s.name)  #'Steve'

    s.name = 'Bill'
    print(s.name)  #'Bill'

    std = Student('Steve')
    del std.name
    print(std.name)  #AttributeError

if __name__ == '__main__':
    main()

