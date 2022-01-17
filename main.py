from english_words import english_words_set
import filters

result = english_words_set

right_place = [["e", 4], ["s", 0], ["h", 1]]
wrong_place = []
wrong = ["c", "l", "o", "v", "a", "d"]

result = filters.word_length_filter(result, 5)

for letter in wrong:
    result = filters.word_wrong_letter(result, letter)

for letter, idx in wrong_place:
    result = filters.word_letter_wrong_place(result, letter, idx)

for letter, idx in right_place:
    result = filters.word_letter_right_place(result, letter, idx)

print(result)

