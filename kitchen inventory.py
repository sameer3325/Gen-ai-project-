kitchen_items = {
    "Rice": 5,
    "Oil": 2,
    "Milk": 1,
    "Eggs": 12
}

def check_inventory():

    for item,qty in kitchen_items.items():

        if qty <= 1:
            print(item,"is running low!")

check_inventory()