# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""This program takes a string of Alphabets and finds the longest substring of continuously increasing order of alphabets"""
s = 'adefgihjilmnpoqstvxuyz'
index = 0
count = 0
substring1 = []
substring1.append(s[index])
list_main = []
#index += 1
for index in range (1,len(s)):
    letter = s[index]
    if letter >= s[index-1]:
        substring1.append(letter)
    else:
        list_main.append(substring1)
        substring1 = []
        substring1.append(letter)
    list_main.append(substring1)
longest_substring = list_main[0]
count += 1
index = len(list_main)
while count < index:
    temp_string = list_main[count]
    if len(longest_substring) < len(temp_string):
        longest_substring = temp_string
        count += 1
    else:
        count += 1
merged_list = []
for ind in range (len(longest_substring)):
    merged_list.extend(longest_substring[ind])
print ("Longest substring in alphabetical order is: " + ''.join(merged_list))


