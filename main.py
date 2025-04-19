#IMPORTS
from stats import word_counting
from stats import characters_counting

#Function to transform a .txt in a long string
def get_book_text (file_path) :
    with open(file_path) as b :
        path_as_string = b.read()
    return path_as_string

#MAIN
book = get_book_text("books/frankenstein.txt") #Book is a long string of the full book
words = book.split() #Words is a list of every word in book, separated
number_of_words = word_counting(words) #Number of words is a count of the number of elements of words list
characters = characters_counting(book)

print(f"{number_of_words} words found in the document")
print(f"Number of characters: {characters}")

