# import secrets
# def private_key(p):
#     if p<1:
#         raise ValueError("Number can not be least than 1")
#     x = [i for i in range(2,p) if all(i%j for j in range(2,min(i,11)))]
#     c = secrets.choice(x)
#     return c  

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