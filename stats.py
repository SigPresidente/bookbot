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

#To divide dictionary "characters" in list of smaller dictionaries with "char" and "value"
#as keys. Then order the small dictionaries based off counts of char
def order_by_count (unordered_dictionary) :
    unordered_list = []
    for char, count in unordered_dictionary.items() :
        smaller_dictionary = {}
        smaller_dictionary["char"] = char
        smaller_dictionary["count"] = count
        unordered_list.append(smaller_dictionary)
    ordered_list = sorted(unordered_list, key=lambda d: d["count"], reverse=True)
    return ordered_list

#To filter only alphanumeric characters from the ordered list
def filter (unfiltered) :
    filtered = []
    for single_dict in unfiltered :
        if (single_dict["char"].isalpha() == True) :
            filtered.append(single_dict)
    return filtered

