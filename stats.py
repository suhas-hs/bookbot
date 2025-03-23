def get_num_words(file_contents):
    return len(file_contents.split())
    

def get_char_map(file_contents):
    char_map = {}
    for char in file_contents.lower():
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1
    return char_map

def sort_on(dict):
    return dict["num"]

def sort_dict(char_map):
    array_dict = []
    for c in char_map:
        if c.isalpha():
            alpha_dict = {"char" : c, "num" : char_map[c]}
            array_dict.append(alpha_dict)
    array_dict.sort(reverse=True, key=sort_on)
    return array_dict
    
