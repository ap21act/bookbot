from stats import get_num_words
from stats import count_character
from stats import book_bot

import sys 
def get_book_text(dir):

    with open(dir) as f:
        file_contents = f.read()
    # do something with f (the file) here

    
    return file_contents




def main():
    if not sys.argv [0]  or len(sys.argv) >2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    file_location = sys.argv [1]
    text = get_book_text(file_location)
    # print(text)
    dict,count=book_bot(text)
    # print(dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_location}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    # print()
    for item in dict :
        if item.isalpha():
            print(f"{item}: {dict[item]}")
    print("============= END ===============")






    

# sys.argv




main()
