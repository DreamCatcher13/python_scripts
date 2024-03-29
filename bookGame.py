import random

def randomList(l):
    """get 2 random books from a list"""
    result = []
    for i in range(2):
        result.append(random.choice(l))
        l.remove(result[i])
    return result

def convertToPairs (l):
    """convert a list with separated books into list of tuples (2 books in a tuple)"""
    if len(l)%2 != 0:
        l.append(" ")
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

books = []

with open("booklist.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        books.append(line.strip())

print("Round 1\n")
roundOne = []

while len(books) != 0:
    pair = randomList(books)
    r = input(f"Select a book:\n 0 {pair[0]}\n 1 {pair[1]}\n")
    roundOne.append(pair[int(r)])

r = 1  # round number

nextRound(roundOne, r)

## gui maybe: open file with books, 2 buttons..

