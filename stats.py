#FUNCTIONS
#To count number of words in a book (list)
def word_counting (words) :
    i = 0
    for word in words :
        i += 1
    return i

#To count characters
def characters_counting (book) :
    characters = {}
    book_lowercase = book.lower()
    for char in book_lowercase :
        if char not in characters :
            characters[char] = 1
        else :
            characters[char] += 1
    return characters
