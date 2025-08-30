def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())

def get_number_characters(text):
    dic = {}
    for char in text:
        char = char.lower()
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    return dic

def sort_on(item):
    return item["num"]

def char_to_sorted_dictionary_list(dictionary):
    l = []
    for k in dictionary:
        l.append({"char": k, "num": dictionary[k]})
    
    l.sort(reverse=True, key = sort_on)
    return l