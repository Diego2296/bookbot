import os 
import sys
from stats import get_num_words, get_char_counts, get_dict_sort

def get_book_text(filepath):
    """
    Take a filepath as an input and returns the contet of the file as a string
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
    

def main():
    """
    Uses get_book_text with the relative path to frankenstein.txt
    to print the entire contents of the book to the console.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_content = get_book_text(book_path)
    num_words = get_num_words(book_content)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_counts = get_char_counts(book_content)
    sorted_chars = get_dict_sort(char_counts)
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")  


# Call main() at the bottom of your file to execute your program.
if __name__ == "__main__":
    main()

