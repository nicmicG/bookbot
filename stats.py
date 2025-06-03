def word_count(book_text):
    num_words = book_text.split()
    return (f"Found {len(num_words)} total words")

def count_characters(book_text):
    #create count of characters in book_text
    lowercase_text = book_text.lower()
    counted_characters = {}
    for character in lowercase_text:
        if character in counted_characters:
            counted_characters[character] += 1
        else:
            counted_characters[character] = 1
    return counted_characters

def sort_on(dict):
    return dict["num"]

def character_sort(counted_characters):
    character_dictionaries = []
    for key, value in counted_characters.items():
        character_dictionary = {
            "char": key,
            "num": value
        }
        character_dictionaries.append(character_dictionary)
        #sort character_dictionaries
    
    character_dictionaries.sort(reverse=True, key=sort_on)
    return character_dictionaries
        #sorted_dictionary.sort()
    #sort the counted characters by count
   