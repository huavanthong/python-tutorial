from typing import TypeVar, Type

# Định nghĩa một biến kiểu dữ liệu generic
SelfType = TypeVar('SelfType')

class DoIPClient:
    @classmethod
    def some_class_method(cls: Type[SelfType]) -> None:
        print(f"This is a class method of {cls}")

# Sử dụng class method
DoIPClient.some_class_method()
