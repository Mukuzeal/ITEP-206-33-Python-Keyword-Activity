# Simple Online Store System using Python Keywords

# 'import' keyword - importing modules
import random as rnd  # 'as' keyword - aliasing module

# 'class' keyword - defining a class for store items
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# 'class' keyword - defining a class for shopping cart
class ShoppingCart:
    def __init__(self):
        self.items = []  # Stores added items
    
    def add_item(self, item):
        self.items.append(item)  # Adding item to cart
    
    def remove_item(self, name):
        # 'for', 'in', 'if', 'break' - finding and removing item
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"{item.name} removed from cart.")
                break
        else:
            print(False)  # 'False' keyword - printed when item not found

    def total_price(self):
        return sum(item.price for item in self.items)  # Using generator expression
    
    def checkout(self):
        if self.items:  # 'if' keyword
            print("Checking out... Your total is:", self.total_price())
            return True
        else:
            print("Cart is empty!")
            return False

# 'def' keyword - defining a function
def apply_discount(price):
    # 'lambda' keyword - short function for discount calculation
    discount = lambda x: x * 0.9  # 10% discount
    return discount(price)

# 'try', 'except', 'finally' keywords - handling errors
try:
    cart = ShoppingCart()

    # Adding items
    cart.add_item(Item("Laptop", 50000))
    cart.add_item(Item("Mouse", 1500))

    # Removing an item
    cart.remove_item("Mouse")

    # 'assert' keyword - checking a condition
    assert cart.total_price() > 0, "Total price should be greater than zero!"

    # 'while' keyword - simulating checkout attempt
    attempts = 3
    while attempts > 0:
        confirm = input("Do you want to checkout? (yes/no): ").lower()
        if confirm == "yes":
            if cart.checkout():
                break  # 'break' keyword - exit loop
        elif confirm == "no":
            print("Checkout canceled.")
            break
        else:
            print("Invalid input, try again.")
        attempts -= 1
    else:
        print("Too many failed attempts.")  # 'else' with while loop

finally:
    print("Thank you for shopping with us!")  # 'finally' keyword

# 'global' keyword - defining a global variable
global discount_applied
discount_applied = True

def apply_global_discount():
    global discount_applied  # Modifying global variable
    discount_applied = True

apply_global_discount()
print("Discount applied:", discount_applied)  # 'True' keyword

# 'nonlocal' keyword - modifying outer variable in nested function
def discount_manager():
    discount_status = "Not Applied"
    
    def apply():
        nonlocal discount_status
        discount_status = "Applied"
    
    apply()
    print("Discount status:", discount_status)

discount_manager()

# 'is', 'not' keywords - identity comparison
order_processed = None
print(order_processed is None)  # True
print(order_processed is not True)  # True

# 'pass' keyword - placeholder for future features
def future_update():
    pass  # No implementation yet

# 'del' keyword - deleting an object
del cart  # Shopping cart is deleted

# 'raise' keyword - raising an error manually
def validate_price(price):
    if price < 0:
        raise ValueError("Price cannot be negative!")

# 'yield' keyword - using generator for order tracking
def order_status():
    yield "Order Placed"
    yield "Order Shipped"
    yield "Order Delivered"

status = order_status()
print(next(status))  # Order Placed
print(next(status))  # Order Shipped
