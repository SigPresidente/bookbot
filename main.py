#Function to transform a .txt in a long string
def get_book_text (file_path) :
    with open(file_path) as b :
        path_as_string = b.read()
    return path_as_string

#Function to count number of elements in a list
def word_counting (words) :
    i = 0
    for word in words :
        i += 1
    return i

#MAIN
#Book is a long string of the full book
book = get_book_text("books/frankenstein.txt")
#Words is a list of every word in book, separated
words = book.split()
#Number of words is a count of the number of elements of words list
number_of_words = word_counting(words)

print(f"{number_of_words} words found in the document")

