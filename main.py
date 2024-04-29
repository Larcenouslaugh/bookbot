def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_num  = get_char_num(text)
    print(f"{num_words} words found in the document")
    print(char_num)

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

main()

