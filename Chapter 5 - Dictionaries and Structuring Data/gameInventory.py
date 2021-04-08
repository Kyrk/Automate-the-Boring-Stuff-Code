#!/usr/bin/env python3
"""
Program that models a player's inventory through a dictionary.
"""
#stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    """Function that prints the contents and total number of items in
    dictionary argument."""
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print("{} {}".format(v, k))
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    """Function that adds items from addedItems argument to inventory argument
    and returns updated dictionary."""
    for item in addedItems:
        inventory.setdefault(item, 0) # Add item to dictionary if DNE
        inventory[item] += 1 # Iterate value
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
