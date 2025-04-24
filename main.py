#IMPORTS
from stats import word_counting
from stats import characters_counting
from stats import order_by_count
from stats import filter
import sys
from sys import argv

#Function to transform a .txt in a long string
def get_book_text (file_path) :
    with open(file_path) as b :
        path_as_string = b.read()
    return path_as_string

#MAIN
if (len(sys.argv) == 2) :
    link = sys.argv[1]
else :
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = get_book_text(link) #Book is a long string of the full book
words = book.split() #Renders the book string in a list of word elements
number_of_words = word_counting(words) #Counts the number of elements of words list
characters = characters_counting(book) #List of characters and relative number of apparition
ordered_by_count = order_by_count(characters) #List of chars ordered by count
filtered_list = filter(ordered_by_count) #Filters the list, eliminating non-alphanumerical values

print("============ BOOKBOT ============")
print(f"Analyzing book found at {link}...")
print("----------- Word Count ----------")
print(f"Found {number_of_words} total words")
print("--------- Character Count -------")
for single_dict in filtered_list :
    print(f"{single_dict["char"]}: {single_dict["count"]}")
print("============= END ===============")
