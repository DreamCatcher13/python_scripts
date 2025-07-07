import random
import pandas
import argparse
from helper import nextRound

parser = argparse.ArgumentParser(description="Argument parser",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--file", 
                    help="Path to file with books",)
parser.add_argument("--scenario", 
                    help="Possible scenarios are 'random-book' or 'book-game'")

args = vars(parser.parse_args())

if args['scenario'] == 'book-game':
    data = pandas.read_excel(args['file'], sheet_name=f'read')
    books = data['Title'].tolist()
    random.shuffle(books)
    nextRound(books, 0)
elif args['scenario'] == 'random-book':
    data = pandas.read_excel('books.xlsx', sheet_name=f'un-read')
    books = data['Title'].tolist()
    random.shuffle(books)
    print(f"Your next book to read: {random.choice(books)}")

## gui maybe: open file with books, 2 buttons..

