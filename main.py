
def main():
    file_location = "books/frankenstein.txt"
    file_contents = read_file(file_location)
    words = split_words(file_contents)
    print(len(words))
    print("test")

def read_file(file):
    with open(file) as f:
        return f.read()

def split_words(s):
    return s.split()

#def count_char():
main()