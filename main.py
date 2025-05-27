from stats import count_words

def get_book_text(filepath: str) -> str:
  with open(filepath) as file:
    book_text = file.read()
  return book_text


def main():
  filepath = "./books/frankenstein.txt"
  book_text = get_book_text(filepath)
  print(f"{count_words(book_text)} words found in the document")

main()