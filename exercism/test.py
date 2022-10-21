
# def is_armstrong_number(number):
#     lena = int(len(str(number)))
#     print(lena)
#     suma = sum([int(i)**lena for i in str(number)])
#     if number == suma:
#         return True
#     return False

# print(is_armstrong_number(154))

# lis=[3,4,6,4,3,1]
# lis = [i for i in lis if i !=3]

# print(lis)

# id = ['uno','dos','tres']
# compara = ['tierra','fuego','aire']
# cual = lambda x:compara[id.index(x)]

# print(cual('uno'))

# def remove_suffix_ness(word):
#     """Remove the suffix from the word while keeping spelling in mind.

#     :param word: str - of word to remove suffix from.
#     :return: str - of word with suffix removed & spelling adjusted.

#     For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
#     """
#     word = word[:-4]
#     if word[-1:]=='i':
#         word = word[:-1]+'y'    
#     print (word)

# remove_suffix_ness('heaviness')

# def adjective_to_verb(sentence, index):
#     """Change the adjective within the sentence to a verb.

#     :param sentence: str - that uses the word in sentence.
#     :param index: int - index of the word to remove and transform.
#     :return: str - word that changes the extracted adjective to a verb.

#     For example, ("It got dark as the sun set", 2) becomes "darken".
#     """
#     word = sentence.split(" ")
#     word = word[index]
#     if word[-1:]==".":
#         word=word[:-1]
#     return word+"en"
    

# #print(adjective_to_verb("His expression went dark.",-1))

# def compare_records(azara_record, rui_record):
#     """Compare two record types and determine if their coordinates match.

#     :param azara_record: tuple - a (treasure, coordinate) pair.
#     :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
#     :return: bool - do the coordinates match?
#     """
#     one = "".join(azara_record[1])
    
#     two = "".join(rui_record[1])

#     return one==two

# #print(compare_records(('Model Ship in Large Bottle', '8A'), ('Harbor Managers Office', ('8', 'A'), 'purple')))

# def clean_up(combined_record_group):
#     """Clean up a combined record group into a multi-line string of single records.

#     :param combined_record_group: tuple - everything from both participants.
#     :return: str - everything "cleaned", excess coordinates and information are removed.

#     The return statement should be a multi-lined string with items separated by newlines.

#     (see HINTS.md for an example).
#     """
#     strin = ""
#     for item in combined_record_group:
#         strin = strin + (f'({item[0]}, {item[2]}, {item[3]}, {item[4]})\n')
#     return strin

# def create_inventory(items):
#     """Create a dict that tracks the amount (count) of each element on the `items` list.

#     :param items: list - list of items to create an inventory from.
#     :return: dict - the inventory dictionary.
#     """
#     items2 = list(dict.fromkeys(items))
#     dicto = {item:items.count(item) for item in items2}
#     return dicto



def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    items2 = list(dict.fromkeys(items))
    dicto = {item:items.count(item) for item in items2}
    inventory = inventory | dicto
    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for key,item in inventory.items():
        num = items.count(key)
        if item != 0:
            item = item-num
            inventory[key]=item
    return inventory
    
print(decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"]))
        
    