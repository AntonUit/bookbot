from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(filepath):
    with open (filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) !=2:
        sys.exit ("Usage: python3 main.py <path_to_book>")
    file = sys.argv[1]
    text = get_book_text(file)
    print (f"Analyzing book found at {file}")
    counted_words=count_words(text)
    print ("---------- Word Count ---------")
    print ("Found", counted_words,"total words")
    sorted_characters=sort_characters(count_characters(text))
    print ("---------- Character Count ---------")
    for item in sorted_characters:
        if item["char"].isalpha():
            print (f"{item["char"]}: {item["num"]}")
    print 
    return


main()
