import random
import pandas
import argparse
from helper import nextRound, shuffleBooks

parser = argparse.ArgumentParser(description="Argument parser",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--file", 
                    help="Path to file with books",)
parser.add_argument("--scenario", 
                    help="Possible scenarios are 'random-book' or 'book-game'")

args = vars(parser.parse_args())

booksData = args['file']
scenario = args['scenario']

if scenario == 'book-game':
    books = shuffleBooks(booksData, 'read')
    nextRound(books, 0)
elif scenario == 'random-book':
    books = shuffleBooks(booksData, 'un-read')
    print(f"Your next book to read: {random.choice(books)}")

## gui maybe: open file with books, 2 buttons..

