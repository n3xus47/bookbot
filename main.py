import sys
from stats import get_num_words, get_num_of_times_each_character, get_sorted_character_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    num_words = get_num_words(book_text)
    chars_dict = get_num_of_times_each_character(book_text)
    sorted_chars = get_sorted_character_list(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
main()