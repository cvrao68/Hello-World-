# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 23:25:23 2018

@author: Veer Rao
"""
test = {'u': [10, 15, 5, 2, 6], 'B': [15]}
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for index in aDict:
        count += len(aDict[index])
    return count
print (how_many(test))