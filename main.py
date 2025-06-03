#main code for bookbot
# Bookbot: A simple book analysis tool

import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

from stats import word_count

from stats import count_characters

from stats import character_sort

def main():
    #deprecated
    #path_to_file = 'books/frankenstein.txt'
    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    character_count = count_characters(book_text)
    sorted_characters = character_sort(character_count)
    print("============ BOOKBOT ============")
    print(f"analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    printable_word_count = word_count(book_text)
    print (printable_word_count)
    print("--------- Character Count -------")
    for character in sorted_characters:
        if character['char'].isalpha() == True:
            print(f"{character['char']}: {character['num']}")
        else:
            continue
    print ("============= END ===============")
main()
    
