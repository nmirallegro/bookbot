# with open('/home/nmirallegro/workspace/github.com/nmirallegro/bookbot/books/frankenstein.txt', 'r') as file:
#     content = file.read()
#     print(content)

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

def get_book_text(path):
    with open(path) as file:
        return file.read()
    
main()