
from stats import wordcount, charactercount, printstats
import sys


def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    count = wordcount(text)
    print(f"{count} words found in the document")
    charcount = charactercount(text)
    printstats(path,count,charcount)
    

main()