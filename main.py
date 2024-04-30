def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_num  = get_char_num(text)
    sort_char = dict(sorted(char_num.items(),reverse=True, key= sort_let))
    print(f"{num_words} words found in the document")
    for key in sort_char:
        print(f"The '{key}' character was found {sort_char[key]} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_char_num(text):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letter_count = {letters: 0 for letters in letters}
    for char in text.lower():
        if char in letters:
            letter_count[char] += 1
    return letter_count

def sort_let(char_num):
    return char_num[1]

main()

