import string
import math as m

# Less than because earlier values represent earlier chars
def rowGreaterThan(r1, r2):
    if(len(r1) != len(r2)): return False
    for i in range(len(r1)):
        if (r1 < r2): return True
        if (r1 == r2): continue
    return False

def wordToRow(word):
    row = [0 for x in range(26)]
    for letter in word:
        posInAlph = string.ascii_lowercase.index(letter)
        row[posInAlph] = row[posInAlph] + 1
    return row

def binaryRowSearch(words, searchRow):
    check = m.ceil(len(words)/2)
    if(len(words) == 1): return words[0][1] if (words[0][0] == searchRow) else None

    if(words[check][0] == searchRow): 
        return words[check][1]
    elif(rowGreaterThan(words[check][0], searchRow)):
        return binaryRowSearch(words[:check], searchRow)
    else:
        return binaryRowSearch(words[check:], searchRow)
    





def binarySearchPrefix(words, search): 
    check = m.ceil(len(words)/2)

    if(len(words) == 1):
        if(hasPrefix(words[0], search)): return True
        return False

    if(hasPrefix(words[check], search)):
        return True
    elif(words[check] > search):
        return binarySearchPrefix(words[:check], search)
    else:
        return binarySearchPrefix(words[check:], search)

def binarySearchWord(words, search): 
    check = m.ceil(len(words)/2)

    if(len(words) == 1 and words[0] != search):
        return False
    elif(len(words) == 1):
        return True

    if(words[check] == search):
        return True
    elif(words[check] > search):
        return binarySearchWord(words[:check], search)
    else:
        return binarySearchWord(words[check:], search)

def hasPrefix(word, prefix):
    plength = len(prefix)
    if(len(word) <= plength):        return False
    elif(word[:plength] != prefix): return False
    return True
