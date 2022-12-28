import math as m 
from row import *

def main():
    f = open('input.txt', 'r')
    dictionary = f.read().lower().splitlines()
    f = open('sortByLength.txt', 'w')

    list = ['zba\n', 'bcde\n', 'ccde\n', 'abc\n', 'xy\n', 'bc\n']
    dictionary = mergeSortByLength(dictionary)
    for word in dictionary:
        f.write(word + "\n")
    f.close()
    

def mergeSortByLength(list):
    if(len(list) == 1 or (len(list) == 2 and greaterThan(list[1], list[0]))): return list
    if(len(list) == 2):                                                       return [list[1], list[0]]
        
    center = m.ceil(len(list)/2)
    l1 = mergeSortByLength(list[:center]) 
    l2 = mergeSortByLength(list[center:])

    newList = []
    for i in range(len(l1) + len(l2)):
        if(len(l1) == 0 or len(l2) == 0): break 
        if(greaterThan(l1[0], l2[0])):    newList.append(l2.pop(0))
        else:                             newList.append(l1.pop(0))
    return(newList + l1 + l2)

def greaterThan(w1, w2):
    if(len(w1) > len(w2)):              return True
    if(len(w1) == len(w2) and rowGreaterThan(wordToRow(w1), wordToRow(w2))): return True
    return False



if __name__ == "__main__":
    main()