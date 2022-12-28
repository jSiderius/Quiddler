import math as m
from row import *

def main():
    f = open('sortByLength.txt', 'r')
    read = f.read().lower().splitlines()
    dictionary = [[]]
    for i in range(len(read)):
        if(len(dictionary) < len(read[i])): 
            dictionary.append([])
        dictionary[len(read[i]) - 1].append((wordToRow(read[i]), read[i]))
    # print(dictionary[1])

    cards = getCards()
    print(findLargest(dictionary, cards))

def findLargest(words, cards):
    if(len(cards) == 1): return None
    word = binaryRowSearch(words[len(cards) - 1], wordToRow(cards))
    if(word != None): return word


    # for word in words[len(cards) - 1]:
    #     if(word[0] == row):
    #         return word[1]

    found = []
    for i in range(len(cards)):
        new = findLargest(words, cards[:i] + cards[i+1:])
        if(new != None): found.append(new)
    if(found == []): return None 
    return max(found, key=len)

def getCards():
    valid_cards = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','qu','in','er','th','cl']
    
    print("Enter your hand as space seperated values: ")
    cards  = input().lower().split()
    for card in cards:
        if card not in valid_cards:
            print("Invalid cards")
            return getCards()
    return cards

if __name__ == "__main__":
    main()