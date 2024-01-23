"""

Refer: https://realpython.com/python-optional-arguments/
"""
# optional_params.py

shopping_list = {
    "Bread": 1,
    "Milk": 2,
    "Chocolate": 1,
    "Butter": 1,
    "Coffee": 1,
}

def show_list():
    for item_name, quantity in shopping_list.items():
        print(f"{quantity}x {item_name}")

show_list()