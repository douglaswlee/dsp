import sys
import os
import csv
from datetime import datetime
import time
import random

# PEP8 NOTES
# Use spaces (4) instead of tabs for indentation
# Max line length for coding is 79 chars
# Place imports at top of the file
# Single-quoted and double-quoted strings are the same, but be consistent

# DATA STRUCTURES
# Lists and tuples
# Similarities: are sequential and ordered (so can be indexed and can have
# sequence operations performed on them: (slicing, length)
# Differences: Lists are mutable and variable length, can modify, add, remove
# elements. Define lists with brackets, tuples with parentheses. Elements in
# tuples correspond to different attributes (in practice), in lists all "same"
# Lists can be used as dictionary keys because of immutability (hashable)

# Lists and sets
# Similarities: mutable collections of objects
# Differences: Sets have unique elements only and are immutable. Sets are not
# ordered so that there is no indexing with sets. Sets are defined with braces
# instead of brackets with lists. Sets support intersection, union and other
# mathematical set operations.
# Performance: Sets are faster for finding an element, because a list needs to
# be searched as a whole to find a match while for sets only a particular position in memory needs to be located.

# FUNCTIONAL TOOLS

# What is lambda?
# Lambda allows us to create anonymous functions (in-line and w/o being named
# using def). Used when function is needed for that is simple (one-line) and
# for a specific short-term purpose (operation on each element of a large list
# for example). For these purposes, lambda functions are passed as arguments
# to other functions which accommodate functions as arguments (map, filter)

# Lambda function takes input list of ints and returns only even numbers, in same order

f = lambda my_list: [x for x in my_list if x % 2 == 0]

# Use "map" to return list which is the square of each item in input list of ints

def sqr(x):
    return x**2

items_list = []
items_squared = map(sqr, items_list)

# Use "filter" to return list which includes items in input list of ints that are multiples of 10

xlist = []
tens_list = filter(lambda x: x % 10 == 0, xlist)

# DATETIME
# Function that computes difference in days between two give dates
# Dates given as strings in '%m-%d-%Y' format

def difference_in_days(date1, date2):
    dt1 = datetime.strptime(date1, '%m-%d-%Y')
    dt2 = datetime.strptime(date2, '%m-%d-%Y')
    return (dt2-dt1).days

# LIST COMPREHENSION
# One-line list comprehension of Farenheit values given list of Celsius values

celsius = []
fahrenheit = [(9/5)*x + 32 for x in celsius]

# STRINGS
# Function returning a string 'Number of donuts: <count>' for a given int count of donuts
# Return string as 'Number of donuts: many' when the count is 10 or more

def donuts(count):
    if count < 10:
        return 'Number of donuts: ' + str(count)
    else:
        return 'Number of donuts: many'

# Function that given a string, returns a string of the first 2/last 2 character
# If string length less than 2 return empty string

def both_ends(s):
    if len(s) >= 2:
        return s[:2]+s[-2:]
    else:
        return ''

# Function that given a string returns the same string but with all occurrences
# of the first character are changed to '*' (but not the first character itself)
# Assume string is length 1 or more

def fix_start(s):
    start = s[0]
    rest_of = s[1:].replace(s[0],'*')
    return start + rest_of

# Function that given strings a and b, returns a single string separated by space
# First two characters of each string (assume length 2+) are swapped

def mix_up(a, b):
    str1 = b[0:2] + a[2:]
    str2 = a[0:2] + b[2:]
    return str1 + ' ' + str2

# Function that given string, if at least length 3, adds 'ing' to its end
# If string already ends in 'ing' add 'ly' instead
# If string is less than length 3, leave unchanged 

def verbing(s):
    if len(s) >= 3 and not s.endswith('ing'):
        return s + 'ing'
    elif len(s) >= 3:
        return s + 'ly'
    else:
        return s

# Function that given a string, finds first appearance of 'not' and 'bad'
# If 'bad' follows 'not' replace the 'not...bad' substring with 'good'

def not_bad(s):
    not_idx = s.find('not')
    bad_idx = s.find('bad')
    if bad_idx < not_idx:
        return s
    else:
        return s[:not_idx] + 'good' + s[(bad_idx+3):]

# Function that divides two strings into halves. If odd, extra char in front half
# For input strings a and b, return a-front + b-front + a-back + b-back

def front_back(s1, s2):
    s1_div = len(s1)//2 if len(s1) % 2 == 0 else len(s1)//2 + 1
    s2_div = len(s2)//2 if len(s2) % 2 == 0 else len(s2)//2 + 1
    return s1[:s1_div] + s2[:s2_div] + s1[s1_div:] + s2[s2_div:]

# LISTS
# Function that given a list of strings, count the strings (of length 2 or more)
# where the first and last chars of the string are the same

def match_ends(s):
    match = 0
    
    for i in s:
        if len(i) >= 2 and i[0] == i[-1]:
            match += 1
    return match

# Function that given a list of strings, returns the sorted list except
# group all the strings beginning with 'x' first

def front_x(words):
    x_only = [i for i in words if i[0] == 'x']
    no_x_only = [i for i in words if i[0] != 'x']
    
    return sorted(x_only) + sorted(no_x_only)

# Function that given a list of non-empty tuples, returns sorted list
# by last element in each tuple

def sort_last(tuples):
    return sorted(tuples, key = lambda x: x[-1])

# Function that given a list of numbers returns a list where all adjacent
# equal elements are reduced to a single element ([1, 2, 2, 3] returns [1, 2, 3])

def remove_adjacent(nums):
    loc = 1
    while loc < len(nums)-1:
        if nums[loc] == nums[loc-1] and nums[loc] == nums[loc+1]:
            nums.pop(loc+1)
            nums.pop(loc-1)
        elif nums[loc] == nums[loc+1]:
            nums.pop(loc+1)
            loc += 1
        elif nums[loc] == nums[loc-1]:
            nums.pop(loc-1)
        else:
            loc += 1
    return nums

# Function that given two sorted lists, returns a sorted merged list
# Should work in linear time

def linear_merge(list1, list2):

    # NAIVE (?) ALSO NOT LINEAR O((m+n) log (m+n))
    #return sorted(list1 + list2)

    # USES ITERATORS (LINEAR?)
    #if len(list1) == 0 and len(list2) == 0:
    #    return list1+list2
    #elif len(list1) == 0:
    #    return list2
    #elif len(list2) == 0:
    #    return list1
    #else:
        #if list1[-1] > list2[-1]:
        #    list1, list2 = list2, list1
        #l_new = []
        #it = iter(list2)
        #pos = next(it)
        #for i in range(len(list1)):
        #    while pos < list1[i]:
        #        l_new.append(pos)
        #        pos = next(it)
        #    l_new.append(list1[i])
        #l_new.append(pos)
        #l_new.extend(it)
        #return l_new

    # SIMPLE SINGLE LOOP EVAL(LINEAR?)    
    l_new = []
    i = 0
    j = 0
        
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            l_new.append(list1[i])
            i += 1
        else:
            l_new.append(list2[j])
            j += 1
    if i == len(list1):
        return l_new + list2[j:]
    if j == len(list2):
        return l_new + list1[i:]

# for comparison
def merge_one(list1, list2):
    return sorted(list1 + list2)

def merge_two(list1, list2):
    l = []
    while list1 and list2:
        if list1[0] < list2[0]:
            l.append(list1.pop(0))
        else:
            l.append(list2.pop(0))
    return l + list1 + list2

list1 = random.sample(range(10**7), 100000)
list2 = random.sample(range(10**7), 100000)

start_time = time.time()
merge_one(list1, list2)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
merge_two(list1, list2)
end_time = time.time()
print(end_time - start_time)

# PARSING
# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# Don't use pandas.

# Following functions will be called like this:
#   footballTable = read_data('football.csv')
#   minRow = get_index_with_min_abs_score_difference(footballTable)
#   print str(get_team(minRow, footballTable))


def read_data(filename):
    # Returns a list of lists representing the rows of the csv file data.

    # Arguments: filename is the name of a csv file (as a string)
    # Returns: list of lists of strings, where every line is split into a list of values. 
    #    ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
    
    with open(filename) as f:
        lines = [x.rstrip().split(',') for x in f]
    return lines


def get_index_with_min_abs_score_difference(goals):
    #Returns the index of the team with the smallest difference
    #between 'for' and 'against' goals, in terms of absolute value.

    #Arguments: parsed_data is a list of lists of cleaned strings
    #Returns: integer row index
    
    GFidx = goals[0].index('Goals')
    GAidx = goals[0].index('Goals Allowed')
    
    min_GD = sys.maxsize
    min_idx= -1
    n = 1
    
    while n < len(goals):
        GD = abs(int(goals[n][GFidx]) - int(goals[n][GAidx]))
        if GD < min_GD:
            min_GD = GD
            min_idx = n
        n += 1
    return min_idx       
    
    
def get_team(index_value, parsed_data):
    #Returns the team name at a given index.
    
    #Arguments: index_value is an integer row index
    #           parsed_data is the output of `read_data` above
               
    #Returns: the team name
    
    return parsed_data[index_value][0]

# COMPLEXITY
# Function given two unsorted lists, return the intersection. Should be O(n)
# An O(n**2) version would be:
# def intersect_lists_1(list1, list2):
#    return [i for i in list1 if i in list2]

def intersect_lists_2(list1, list2):

    # NAIVE (?)
    #return set(list1) & set(list2)

    # SORT THEN TRAVERSE BOTH LISTS AT ONCE
    # THIS IS NOT LINEAR BECAUSE SORTING IS O(N LOG N)
    # THE COMBINED TRAVERSAL IS O(N**2) B/C POP IS O(N) BUT CAN BE MADE O(N)
    #L1 = sorted(set(list1))
    #L2 = sorted(set(list2))
    #Lnew = []
    
    #while L1 and L2:
    #    if L1[0] > L2[0]:
    #        L2.pop(0)
    #    elif L1[0] < L2[0]:
    #        L1.pop(0)
    #    else:
    #        Lnew.append(L1[0])
    #        L1.pop(0)
    #        L2.pop(0)
    #return Lnew

    # O(N) VERSION STORING ONE LIST'S ELEMENTS AS DICT THEN TRAVERSE OTHER
    #d1 = dict.fromkeys(list1)
    
    #Lnew = []

    # for j in list2:
    #    if j in d1:
    #         Lnew.append(j)
    
    # return Lnew

    # O(N) VERSION STORING ONE LIST'S ELEMENTS AS SET THEN TRAVERSE OTHER
    L1 = set(list1)
    L = []
    
    for i in list2:
        if i in L1:
            L.append(i)      
            
    return L

# Function that given an unsorted list with duplicates, returns list with duplicates removed
# Aim for linear time O(n)
def remove_duplicates(somelist):
    # NAIVE (?), only one that "worked"
    return set(somelist)

    # VERSION USING DICT TO STORE FIRST INDEX OF EACH LIST ELEMENT
    #d = {i: somelist.index(i) for i in somelist}
    #l_new = []

    #for i,v in enumerate(somelist):
    #    if d[v] == i:
    #        l_new.append(v)
    #return l_new

    # VERSION THAT SORTS THEN TRAVERSES FOR DUPLICATES (NOT O(N))    
    #L = sorted(somelist)
    #i = 1
    #j = 0
    #Lnew = [L[0]]
    
    #while i < len(L):
     #   if L[i] != Lnew[j]:
      #      j += 1
     #       Lnew.append(L[i])
       # i += 1

    # VERSION(IN-PLACE) USING SET TO STORE EACH UNIQUE ELEMENT AND PLACE AT FRONT OF ORIGINAL LIST
    #s = set()
    #j = 0
    
    #for i in somelist:
    #     if i not in s:
    #        s.add(i)
    #        somelist[j] = i
    #        j += 1
    #del somelist[j:]
