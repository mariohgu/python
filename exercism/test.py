# import secrets
# def private_key(p):
#     if p<1:
#         raise ValueError("Number can not be least than 1")
#     x = [i for i in range(2,p) if all(i%j for j in range(2,min(i,11)))]
#     c = secrets.choice(x)
#     return c  

<<<<<<< HEAD
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
        
    
=======
# def public_key(p, g, private):
#     p = private_key(p)
#     g = private_key(g)
#     a = secrets.choice(range(2,private))
#     A = (pow(g,a,p))
#     return A

# def secret(p, public, private):
#     S = public_key(p,public,private)
#     return S

# print(secret(23,5,6))

# p = private_key(300)
# g = private_key(200)

# a = secrets.choice(range(2,18))
# b = secrets.choice(range(2,3))


# A = (pow(g,a))%p
# B = (pow(g,b))%p

# S = (pow(B,a))%p
# H = (pow(A,b))%p

# if S==H:
#     print('yep')
# else:
#     print('nop')
from statistics import mean
import math


# def approx_average_is_average(hand):
#     """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

#     :param hand: list - cards in hand.
#     :return: bool - does one of the approximate averages equal the `true average`?
#     """
#     ext = mean(hand[:1]+(hand[-1:]))
#     inde = math.floor(len(hand)/2)
#     print(ext, inde)
#     if mean(hand)==ext or mean(hand)==hand[inde]:
#         return True
#     return False

# print(approx_average_is_average([3, 6, 9, 12, 150]))

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
#     even = mean([j for i,j in enumerate(hand) if i%2==0])
#     odd = mean([j for i,j in enumerate(hand) if i%2!=0])
#     print (even)
#     print(odd)
#     print(hand[-1])
#     if even == odd:
#         return True
#     return False

# print(average_even_is_average_odd([1, 2, 3,4]))

# def student_ranking(student_scores, student_names):
#     """Organize the student's rank, name, and grade information in ascending order.

#     :param student_scores: list - of scores in descending order.
#     :param student_names: list - of string names by exam score in descending order.
#     :return: list - of strings in format ["<rank>. <student name>: <score>"].
#     """
#     new = []
#     for val in range (0,len(student_scores)):
#         new.append(f'{val+1}. {student_names[val]}: {student_scores[val]}')
#     return new

# print(student_ranking([100, 98, 92, 86, 70, 68, 67, 60], ['Rui', 'Betty', 'Joci', 'Yoshi', 'Kora', 'Bern', 'Jan', 'Rose']))

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    tre=[]
    # tre = [val for ind,val in enumerate(student_info) if student_info[ind][1]==100]
    for ind,val in enumerate(student_info):
        if student_info[ind][1]==100:
            tre = val.copy()
            break
    return tre
    
    return tre
#print(perfect_score(student_info=[['Joci', 100], ['Vlad', 100], ['Raiana', 100], ['Alessandro', 100], ['Joci', 100]]))
#print(perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]]))
#print(perfect_score(student_info=[["Charles", 90], ["Tony", 80]]))
print(perfect_score([]))
>>>>>>> bbef0ec2fbbd263b04dc891bf1d03dcb4dfe0b94
