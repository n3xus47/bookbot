def get_num_words(text):
    return len(text.split())

def get_num_of_times_each_character(text):
    lower_text = text.lower()
    char_counts = {}
    for char in lower_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def get_sorted_character_list(char_counts_dict):
    char_list = []
    for char, count in char_counts_dict.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list