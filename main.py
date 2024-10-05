def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(get_word_count(text))
    dic = get_char_frequency(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f" {get_word_count(text)} words found in the document")
    dic2  = [{
        'char' : c , 'count': dic[c]
        }
        for c in dic
        ]
    def sort_on(dict):
        return dict['count']
    dic2.sort(reverse=True,key=sort_on)
    for d in dic2:
        char = d['char']
        count = d['count']
        if char.isalpha():
            print(f"The {char} character was found {count} times")
    print("--- End report ---")
def get_word_count(text):
    return len(text.split())

def get_char_frequency(text):
    text = text.lower()
    dic = {}
    for c in text:
        if c in dic:
            dic[c]+=1
        else:
            dic[c] = 1
    return dic

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
