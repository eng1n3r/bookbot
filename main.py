
def main():
    file_location = "books/frankenstein.txt"
    file_contents = read_file(file_location)
    words = split_words(file_contents)
    characters = count_char(words)
    sorted_list = sorter(characters)
    printer(sorted_list, len(words), file_location)
    #print(sorted_list)
    
    #print(characters)
    #test()
    
    # print(words[0:10])
    # print(len(words))

def read_file(file):
    with open(file) as f:
        return f.read()

def split_words(s):
    return s.split()

def count_char(words):
    my_dict = dict()
    for w in words:
        for c in w.lower():
            my_dict[c] = my_dict.get(c, 0) + 1
    return my_dict

def sort_on(dict):
    return dict["Count"]

def sorter(d):
    new_lst = [{'Char': key, 'Count': value} for key, value in d.items() if key.isalpha()]
    new_lst.sort(reverse=True, key=sort_on)
    return new_lst

def printer(lst, total, location):
    char_key = "Char"
    val_key = "Count"
    print(f"--- Begin report of {location} ---")
    print(f"{total} words found in the document\n")
    for l in lst:
        print(f"The '{l[char_key]}' character was found {l[val_key]} times")
    print("--- End report ---")

def test():
    lst = ["hello", "Yes", "four", "EeeC", "abc"]
    print(count_char(lst))


main()