
def word_length_filter(words, desired_length):
    filtered_words = []
    for word in words:
        if len(word)==desired_length:
            filtered_words.append(word)
    return filtered_words

def word_letter_right_place(words, letter, place_idx):
    filtered_words = []
    for word in words:
        if word[place_idx]==letter:
            filtered_words.append(word)
    return filtered_words

def word_letter_wrong_place(words, letter, place_idx):
    filtered_words = []
    for word in words:
        if word[place_idx]!=letter and letter in word:
            filtered_words.append(word)
    return filtered_words

def word_wrong_letter(words, wrong_letter):
    filtered_words = []
    for word in words:
        if wrong_letter not in word:
            filtered_words.append(word)
    return filtered_words