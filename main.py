import sys

from stats import get_num_chars, get_num_words, sort_chars

def get_book_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bpath = sys.argv[1]
    print("============ BOOKBOT ============")
    book_text = get_book_text(bpath)
    print(f"Analyzing book found at {bpath} ...")
    print("----------- Word Count ----------")
    get_num_words(book_text)
    print("--------- Character Count -------")
    for res in sort_chars(get_num_chars(book_text)):
        if res[0].isalpha():
            print(f"{res[0]}: {res[1]}")
    print("============= END ===============")
main()
