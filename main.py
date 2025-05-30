from stats import count_words, order_characters
import sys

def get_book_text(filepath: str) -> str:
  with open(filepath) as file:
    book_text = file.read()
  return book_text


def main():
    if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    characters = order_characters(book_text)
    char_counts = [f"{char_count['char']}: {char_count['num']}" 
                   for char_count in characters 
                   if char_count['char'].isalpha()]
    print('\n'.join(char_counts))
    print("============= END ===============")

main()
