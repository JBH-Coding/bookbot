def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict[str,int]:
    count = dict()
    for char in text:
      if char.lower() not in count:
         count[char.lower()] = 1
      else:
         count[char.lower()] += 1
    return count

def sort_dict(datum: dict) -> int:
   return datum["num"]

def order_characters(text: str)->list[dict]:
   char_dict = count_characters(text)
   dict_list = [{"char" : key, "num" : count} for key, count in char_dict.items()]
   dict_list.sort(reverse=True, key=sort_dict)
   return dict_list