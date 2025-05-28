
def get_num_words(text):
    """
    Accepts the text from the book as a string and returns the number of words in the string.
    """
    words = text.split()
    return len(words)

def get_char_counts(text):
    """
    Accepts the text from the book as a string and returns a dictionary
    with the count of each character (lowercased) in the string.
    """
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char]+=1
        else:
            char_counts[char] = 1
    return char_counts


def get_dict_sort(char_counts):
    """
    Takes a dictionary of character counts and returns a sorted list of dictionaries,
    each with 'char' and 'num' keys, sorted by count descending.
    Only includes alphabetical characters.
    """
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list