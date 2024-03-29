def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    items2 = list(dict.fromkeys(items))
    dicto = {item: items.count(item) for item in items2}
    return dicto


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


def decrement_items(inventory, items):
    for item in items:
        if inventory[item] > 0:
            inventory[item] -= 1
        else:
            inventory[item] = 0

    return inventory


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]


def list_inventory(inventory):
    """Implement the list_inventory() function that takes an inventory and returns a list of (item, quantity) tuples. The list should only include the available items (with a quantity greater than zero):

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    # return [(k, v) for k, v in inventory.items() if v > 0]
    lista = []
    for key, item in inventory.items():
        if item > 0:
            lista.append((key, item))
    return lista


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.
    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """


x = ("key1", "key2", "key3")
y = 0

thisdict = create_inventory(x)
z = ["key1", "key1", "key2", "key7"]


dict = add_items(thisdict, z)

print(dict)
print(list_inventory({"coal": 15, "diamond": 3, "wood": 67, "silver": 0}))

recipe = {
    "Banana Bread": {
        "Banana": 1,
        "Apple": 1,
        "Walnuts": 1,
        "Flour": 1,
        "Eggs": 2,
        "Butter": 1,
    },
    "Raspberry Pie": {"Raspberry": 1, "Orange": 1, "Pie Crust": 1, "Cream Custard": 1},
}

recipe2 = (
    "Banana Bread",
    {
        "Banana": 4,
        "Walnuts": 2,
        "Flour": 1,
        "Eggs": 2,
        "Butter": 1,
        "Milk": 2,
        "Eggs": 3,
    },
)

recipe3 = update_recipes(recipe, recipe2)
print(recipe3)
