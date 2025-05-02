def getItem(x):
    """
    This function simulates a drive-thru order by returning a random item from the menu.
    """
    import random

    menu = [
        "Burger",
        "Fries",
        "Soda",
        "Salad",
        "Chicken Nuggets",
        "Ice Cream",
        "Coffee",
        "Milkshake"
    ]

    if x < 0 or x >= len(menu):
        return None
    print(f"Your order is: {menu[x]}")
    
def welcome():
    """
    This function simulates a drive-thru welcome message.
    """
    print("Welcome to the Drive-Thru! How can I help you today?")

def main():
    """
    Main function to run the drive-thru simulation.
    """
    welcome()
    getItem(int(input("Please enter the item number (0-7): ")))
    
main()