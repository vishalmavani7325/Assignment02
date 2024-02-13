    # Module – 3 (Collections, functions and Modules)



# # 1  What is List? How will you reverse a list?

# # Reversing a List in Place. As we discussed earlier, the reverse() method reverses a list in place, meaning it modifies the original list.

# list1=[1,2,3,4,5,6,7]
# print(list1)
# list1.reverse()
# print(list1)

# # How will you remove last object from a list?
# # Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]? 


# list1=[2,33,222,14,25]
# list2=list1[-1]
# print(list2)

# # Difference Between append() and extend() in Python

# accepts as input an iterable (such as a list or tuple). The append() function adds the full input to the list as a single item. extend() adds each item to the list independently after iterating through each one in the input

# # Write a Python function to get the largest number, smallest num and sum
# # of all from a list. 

# list1=[1,2,3,4,5,6,7]
# print(min(list1))
# print(max(list1))
# total=0
# for ele in range(0, len(list1)):
#     total = total + list1[ele]
# print("Sum of all elements in given list: ", total)


# # How will you compare two lists? 
   
# def compare(l1,l2):
#     l1.sort()
#     l2.sort()
#     if(l1==l2):
#         return 'equal'
#     else:
#         return 'not equal'
        
# list1=[2,3,5]
# list2=[5,3,2]
# print("coparision",compare(list1,list2))
        
        
        
# list1=[1,3,2]
# list2=[2,3,1]
# l1=list1.sort()
# l2=list2.sort()
# if l1==l2:
#     print('equal')
# else:
#     print('not equal')


# # Write a Python program to count the number of strings where the string
# # length is 2 or more and the first and last character are same from a given
# # list of strings. 


# a=input('enter a list: ')
# print(a)
# count=0
# for word in a:
#     if len(word)>=2 and word[-1]==word[0]:
#         count=count+1
# print(count)
    
    
# # Write a Python program to remove duplicates from a list. 

# list1=[1,2,3,4,5,5,6,6,7,7,8]

# def duplicates_value(duplist):
#     finl_list=[]
#     for ele in duplist:
#         if ele not in finl_list:
#             finl_list.append(ele)
            
#     return finl_list

# print(duplicates_value(list1))


# # Write a Python program to check a list is empty or not. 

# def Enquiry(lis1):
#     if len(lis1) == 0:
#         return 0
#     else:
#         return 1
 
# lis1 = []
# if Enquiry(lis1):
#     print("The list is not empty")
# else:
#     print("Empty List")

# # Write a Python function that takes two lists and returns true if they have
# # at least one common member. 

# def common(l1,l2):
#     flag=False
#     for x in l1:
#         for y in l2:
#             if x==y:
#                 flag=True
#                 return flag
            
# print(common([1,2,3,4,5], [5,6,7,8,9]))
# print(common([1,2,3,4,5], [6,7,8,9]))            

# # Write a Python program to generate and print a list of first and last 5
# # elements where the values are square of numbers between 1 and 30. 

# def value():
#     l=list()
#     for i in range(1,30+1):
#         l.append(i**2)
#     print(l[:5])
#     print(l[-5:])

# value()


# # Write a Python function that takes a list and returns a new list with unique
# # elements of the first list. 


# def unique_list(l):
#     x=[]
    
#     for a in l:
#         if a not in x:
#             x.append(a)
            
#     return x

# print(unique_list([1,2,3,3,4,4,5,5,6,7,7,8]))


# # Write a Python program to convert a list of characters into a string. 

# def convert(s):
#     new=""
    
#     for i in s:
#         new=new+i
        
#     return new

# s=['m','a','v','a','n','i']
# print(convert(s))


# Write a Python program to select an item randomly from a list. 

# xx



# # Write a Python program to find the second smallest number in a list

# l1=[11,35,33,44,55,66,77]
# l1.remove(min(l1))
# print(min(l1))


# # Write a Python program to get unique values from a list 


# def unique(list1):
#     unique_list=[]
    
#     for i in list1:
#         if i not in unique_list:
#             unique_list.append(i)
#     for i in unique_list:
#         print(i)
        
# list1 = [10, 20, 10, 30, 40, 40]
# print("the unique values from 1st list is")
# unique(list1)
 
# # Write a Python program to check whether a list contains a sub list 

# def is_sublist(main_list, sublist):
#     main_tuple = tuple(main_list)
#     sublist_tuple = tuple(sublist)

    
#     for i in range(len(main_tuple) - len(sublist_tuple) + 1):
#         if main_tuple[i:i+len(sublist_tuple)] == sublist_tuple:
#             return True
#     return False


# main_list = [1, 2, 3, 4, 5, 6, 7]
# sublist = [3, 4, 5]

# if is_sublist(main_list, sublist):
#     print("Sublist found in the main list.")
# else:
#     print("Sublist not found in the main list.")



# # Write a Python program to split a list into different variables. 

# string=['vishal','s','mavani']

# a,b,c=string
# print(a)
# print(b)
# print(c)




# # # What is tuple? Difference between list and tuple. 

# # In Python, a tuple is a collection data type that is similar to a list but with some key differences. Here are the main differences between lists and tuples:

# # Mutability:

# # Lists are mutable, meaning their elements can be modified after the list is created. You can add, remove, or change elements in a list.
# # Tuples are immutable, meaning once a tuple is created, its elements cannot be modified, added, or removed. The structure of a tuple remains fixed.
# # Syntax:

# # Lists are defined using square brackets [ ].
# # Tuples are defined using parentheses ( ).
# # Usage:

# # Use lists when you have a collection of items that may need to be modified, such as when you're working with dynamic data or sequences that can change over time.
# # Use tuples when you have a collection of items that should remain constant throughout the program's execution, such as when you're working with fixed data or sequences that should not change.
# # Performance:

# # Since tuples are immutable, they are generally faster to access than lists because Python can make certain optimizations knowing that the data will not change.
# # Lists may be more suitable for operations that involve frequent modifications, such as adding or removing elements.
# # Here's an example demonstrating the syntax and usage of lists and tuples:

# my_list = [1,2,3,4,5]
# print("List:", my_list)

# # Example of a tuple
# my_tuple = (1,2,3,4,5,6)
# print("Tuple:", my_tuple)


# #  Write a Python program to create a tuple with different data types. 
# my_tuple = (1, "hello", 3.14, True)
# print("Tuple with different data types:", my_tuple)


# # Write a Python program to create a tuple with numbers.  

# number_tuple = (1, 2, 3, 4, 5)
# print("Tuple with numbers:", number_tuple)


# # Write a Python program to convert a tuple to a string. 

# def convert(tuple):
#     str=''
#     for i in tuple:
#         str=str+i
#     return str
# tuple= ('m','a','v','a','n','i')
# str=convert(tuple)
# print(str)



# # Write a Python program to check whether an element exists within a tuple

# def element_exists_in_tuple(element, tup):
#     return element in tup


# my_tuple = (1, 2, 3, 4, 5)
# element_to_check = 3

# if element_exists_in_tuple(element_to_check, my_tuple):
#     print(f"The element {element_to_check} exists in the tuple.")
# else:
#     print(f"The element {element_to_check} does not exist in the tuple.")


# # Write a Python program to find the length of a tuple

# def tuple_length(tup):
#     return len(tup)

# my_tuple = (1, 2, 3, 4, 5)
# length = tuple_length(my_tuple)
# print("Length of the tuple:", length)


# # Write a Python program to convert a list to a tuple

# def list_to_tuple(lst):
#     return tuple(lst)

# my_list = [1, 2, 3, 4, 5]
# converted_tuple = list_to_tuple(my_list)
# print("Converted tuple:", converted_tuple)


# # Write a Python program to reverse a tuple.


# def reverse_tuple(tup):
#     return tup[::-1]

# my_tuple = (1, 2, 3, 4, 5)
# reversed_tuple = reverse_tuple(my_tuple)
# print("Reversed tuple:", reversed_tuple) 



# # Write a Python program to replace last value of tuples in a list. 

# def replace_last_value(tuples_list, new_value):
#     updated_tuples_list = []
#     for tup in tuples_list:
#         new_tuple = tup[:-1]
#         new_tuple += (new_value,)
#         updated_tuples_list.append(new_tuple)
#     return updated_tuples_list

# original_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# new_value = 10
# updated_list = replace_last_value(original_list, new_value)
# print("Updated list:", updated_list)


# # Write a Python program to find the repeated items of a tuple.

# def find_repeated_items(tup):
#     repeated_items = []
#     for item in tup:
#         if tup.count(item) > 1 and item not in repeated_items:
#             repeated_items.append(item)
#     return repeated_items

# my_tuple = (1, 2, 3, 4, 2, 5, 3, 6, 7, 3)
# repeated_items = find_repeated_items(my_tuple)
# print("Repeated items in the tuple:", repeated_items)


# # Write a Python program to remove an empty tuple(s) from a list of tuples. 


# list_1 =  [(), ('okay','10','11'), (), ('lock', 'key'),  
#           ('kite', '12'),()] 

# filter_items = filter(lambda x: x != (), list_1)
# remove_tuples = list(filter_items)
# print(remove_tuples)


# # Write a Python program to unzip a list of tuples into individual lists. 

# l = [(1, 2), (3, 4), (8, 9)]
# result = list(zip(*l))
# print(result)



# #  Write a Python program to convert a list of tuples into a dictionary. 

# l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
# d = {}
# for a, b in l:
#     d.setdefault(a, []).append(b)

# print(d) 

# # How will you create a dictionary using tuples in python?

# tuples_list = [("a", 1), ("b", 2), ("c", 3)]
# my_dict = {key: value for key, value in tuples_list}
# print(my_dict)


# # Write a Python script to concatenate following dictionaries to create a
# # new one. 

# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dic4 = {}

# for d in (dic1, dic2, dic3):
#     dic4.update(d)
# print(dic4) 



# # Write a Python script to check if a given key already exists in a
# # dictionary.

# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# def is_key_present(x):
#     if x in d:
#         print('Key is present in the dictionary')
#     else:
#         print('Key is not present in the dictionary')

# is_key_present(5)
# is_key_present(9) 


# #  How Do You Traverse Through A Dictionary Object In Python? 

# grades = {'John': 85, 'Emily': 92, 'Lucas': 78}
# for key in grades:
#     print(key, grades[key])



# # How Do You Check The Presence Of A Key In A Dictionary? 

# my_dict = {'a': 1, 'b': 2, 'c': 3}

# if 'a' in my_dict:
#     print("'a' key exists in the dictionary.")
# else:
#     print("'a' key does not exist in the dictionary.")


# # Write a Python script to print a dictionary where the keys are numbers
# # between 1 and 15.

# d = dict()

# for x in range(1, 16):
#     d[x] = x ** 2
# print(d)


# #  Write a Python program to check multiple keys exists in a dictionary 


# student = {
#   'name': 'Alex',
#   'class': 'V',
#   'roll_id': '2'
# }

# print(student.keys() >= {'class', 'name'})
# print(student.keys() >= {'name', 'Alex'})
# print(student.keys() >= {'roll_id', 'name'}) 


# #  Write a Python script to merge two Python dictionaries 

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}

# dict1.update(dict2)
# print("Merged dictionary:", dict1)


# # Write a Python program to map two lists into a dictionary

# keys = ['red', 'green', 'blue']

# values = ['#FF0000', '#008000', '#0000FF']

# color_dictionary = dict(zip(keys, values))
# print(color_dictionary)



# # Write a Python program to combine two dictionary adding values for
# # common keys.
# # d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}


# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# for key in d2:
#     if key in d1:
#         d2[key] = d2[key] + d1[key]
#     else:
#         pass
         
# print(d2)

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3 = dict(d1) # don't do `d3=d1`, you need to make a copy
# d3.update(d2) 

# for i, j in d1.items():
#     for x, y in d2.items():
#         if i == x:
#             d3[i]=(j+y)
# print(d3)



# #  Write a Python program to print all unique values in a dictionary. 


# L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# print("Original List: ", L)

# u_value = set(val for dic in L for val in dic.values())
# print("Unique Values: ", u_value) 


# #  Why Do You Use the Zip () Method in Python? 


# #  The zip() function in Python is used to combine two or more iterable dictionaries into a single iterable, where corresponding elements from the input iterable are paired together as tuples. When using zip() with dictionaries, it pairs the keys and values of the dictionaries based on their position in the dictionary


   
# stocks = ['TATA', 'IRCF', 'ADANIGREEN']
# prices = [2175, 1127, 2750]
 
# new_dict = {stocks: prices for stocks,
#             prices in zip(stocks, prices)}
# print(new_dict)



# Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.
# Sample data: {'1': ['a','b'], '2': ['c','d']}
# Expected Output:
# ac ad bc bd


# # Write a Python program to find the highest 3 values in a dictionary 

# my_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 50, 'e': 40}
# sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

# highest_3 = sorted_items[:3]
# print("Highest 3 values in the dictionary:", highest_3)



# def highest_3_values(dictionary):
#     sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
#     highest_3 = sorted_items[:3]
#     return highest_3

# my_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 50, 'e': 40}
# highest_values = highest_3_values(my_dict)
# print("Highest 3 values in the dictionary:", highest_values)


# # Write a Python program to combine values in python list of dictionaries.
# # Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
# # 300}, o {'item': 'item1', 'amount': 750}]
# # Expected Output:
# # Counter ({'item1': 1150, 'item2': 300}) 


# from collections import Counter
# data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

# combined_values = Counter()
# for d in data:
#     combined_values[d['item']] += d['amount']

# print("Combined values:", combined_values)




# # Write a Python program to create a dictionary from a string.
# # Note: Track the count of the letters from the string.
# # Sample string: 'w3resource'
# # Expected output:
# # {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

# sample_string = 'w3resource'

# char_counts = {}
# for char in sample_string:
#     char_counts[char] = char_counts.get(char, 0) + 1
# print("Character counts:", char_counts)


# # Write a Python function to calculate the factorial of a number (a
# # nonnegative integer) 

# number = int(input("Enter a non-negative integer: "))
# if number < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     factorial_result = 1
#     for i in range(1, number + 1):
#         factorial_result *= i
#     print("Factorial of", number, "is", factorial_result)


# # Write a Python function to check whether a number is in a given range

# def check_in_range(number, lower, upper):
#     return number in range(lower, upper + 1)

# number = 5
# lower_bound = 1
# upper_bound = 10

# if check_in_range(number, lower_bound, upper_bound):
#     print(f"{number} is in the range [{lower_bound}, {upper_bound}]")
# else:
#     print(f"{number} is not in the range [{lower_bound}, {upper_bound}]")


# # Write a Python function to check whether a number is perfect or not. 

# def is_perfect_number(number):
#     if number <= 0:
#         return False
#     divisor_sum = 0
#     for i in range(1, number):
#         if number % i == 0:
#             divisor_sum += i
#     return divisor_sum == number

# number = 28
# if is_perfect_number(number):
#     print(f"{number} is a perfect number.")
# else:
#     print(f"{number} is not a perfect number.")


# # Write a Python function that checks whether a passed string is
# # palindrome or not 

# def is_palindrome(s):
#     s = ''.join(char.lower() for char in s if char.isalnum())
#     return s == s[::-1]

# string = "A man, a plan, a canal, Panama"
# if is_palindrome(string):
#     print(f"'{string}' is a palindrome.")
# else:
#     print(f"'{string}' is not a palindrome.")




# #  How Many Basic Types Of Functions Are Available In Python? 


# Built-in Functions: len(), type(), range()
# User-Defined Functions:
# Anonymous Functions 


# # How can you pick a random item from a list or tuple? 

# import random

# # list
# my_list = [1, 2, 3, 4, 5]

# random_item = random.choice(my_list)
# print("Random item from the list:", random_item)


# # tuple
# my_tuple = (1, 2, 3, 4, 5)

# random_item = random.choice(my_tuple)
# print("Random item from the tuple:", random_item)


# # How can you pick a random item from a range? 
# import random

# my_range = range(1, 11)  
# random_item = random.choice(list(my_range))
# print("Random item from the range:", random_item)


# #  How can you get a random number in python? 

# import random

# random_number = random.random()
# print("Random number:", random_number)
 
 
# # How will you randomizes the items of a list in place? 
 
# import random
# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# print("Randomized list:", my_list)



#  Write a Python program to read a random line from a file. ???????????

#  Write a Python program to convert degree to radian ????????





# # Write a Python program to calculate the area of a trapezoid 

# base1 = float(input("Enter the length of the first base: "))
# base2 = float(input("Enter the length of the second base: "))
# height = float(input("Enter the height of the trapezoid: "))

# area = ((base1 + base2) * height) / 2
# print("The area of the trapezoid is:", area)


# # Write a Python program to calculate the area of a parallelogram 

# base_length = float(input("Enter the length of the base: "))
# height = float(input("Enter the height of the parallelogram: "))

# area = base_length * height

# print("The area of the parallelogram is:", area)


# Write a Python program to calculate surface volume and area of a
# cylinder ????????



# # Write a Python program to returns sum of all divisors of a number

# number = int(input("Enter a number: "))
# divisor_sum = 0
# for i in range(1, number + 1):
#     if number % i == 0:
#         divisor_sum=divisor_sum+ i
# print("Sum of divisors of", number, "is:", divisor_sum)



# # Write a Python program to find the maximum and minimum numbers
# # from the specified decimal numbers.

# decimal_numbers = [3.14, 2.718, 1.618, 4.669, 0.577]

# maximum_number = max(decimal_numbers)
# minimum_number = min(decimal_numbers)

# print("Maximum number:", maximum_number)
# print("Minimum number:", minimum_number)

