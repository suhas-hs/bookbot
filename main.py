import sys
from stats import (
    get_num_words, 
    get_char_map, 
    sort_dict
)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    file_path = sys.argv[1]
    print(f"Analyzing book found at {file_path}...")
    file_contents = get_book_text(file_path)
    print("----------- Word Count ----------")
    num_words = get_num_words(file_contents)
    print(f"Found {num_words} total words")
    char_map = get_char_map(file_contents)
    sorted_dict = sort_dict(char_map)
    print("--------- Character Count -------")
    for dict in sorted_dict:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")
main()