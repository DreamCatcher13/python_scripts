import random
import pandas

def convertToPairs (l):
    """convert a list with separated books into list of tuples (2 books in a tuple)"""
    if len(l)%2 != 0:
        l.append("Filler")
    return [(l[i], l[i+1]) for i in range(0,len(l),2)]

def nextRound(l, n):
    """game itself, asks you to choose between 2 books"""
    if len(l) == 1:
        print(f"The Winner is: {l[0]}")
    elif len(l) > 1:
        n += 1
        pairs = convertToPairs(l)
        newL = []
        print(f"\nRound {n}\n")
        for i in range(len(pairs)):
            r = input(f"Select a book:\n 0 {pairs[i][0]}\n 1 {pairs[i][1]}\n")
            newL.append(pairs[i][int(r)]) 
        nextRound(newL, n)

def shuffleBooks(booksFile, sheet):
    """takes data and returns a list of books in random order"""    
    data = pandas.read_excel(booksFile, sheet)
    books = data['Title'].tolist()
    random.shuffle(books)
    return books