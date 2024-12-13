import random
import pandas
import argparse

parser = argparse.ArgumentParser(description="Argument parser",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("file", help="Path to file with books")

args = vars(parser.parse_args())

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


excel_df = pandas.read_excel('books.xlsx', sheet_name=f'2024')
books = excel_df['Title'].tolist()
random.shuffle(books)

nextRound(books, 0)

## gui maybe: open file with books, 2 buttons..

