from english_words import english_words_set
import filters

result = english_words_set

right_place = [["p", 0]]
wrong_place = [["p", 3], ["p", 1], ["o", 0], ["o", 1]]
wrong = ["s", "l", "e", "t", "i", "u", "m", "a", "c", "h"]

result = filters.word_length_filter(result, 5)

for letter in wrong:
    result = filters.word_wrong_letter(result, letter)

for letter, idx in wrong_place:
    result = filters.word_letter_wrong_place(result, letter, idx)

for letter, idx in right_place:
    result = filters.word_letter_right_place(result, letter, idx)

result = filters.sort_by_diversity(result)

print(result)

