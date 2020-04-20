# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 08:04:37 2018

@author: Veer Rao
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    valueList = []
    keyList = []
    countKey = 0
    for ind in aDict:
        countKey = len(aDict[ind])
        keyList.append(ind)
        valueList.append(countKey)
    if len(valueList) == 0:
        return
    else:
        for item in valueList:
            if valueList[item] == max(valueList):
                return keyList[item]
    
test = {'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}
print (biggest(test))
        