from stats import *
import sys

def main():
    if(len(sys.argv) == 1):
        print("No file path provided. Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    


    
    
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    char_count = char_to_sorted_dictionary_list(get_number_characters(text))
        

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in char_count:
        if d["char"].isalpha():
            print(f"'{d["char"]}: {d["num"]}'")
    print("============= END ===============")

main()