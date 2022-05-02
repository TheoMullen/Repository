import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

word_dict = {row.letter: row.code for index, row in nato_alphabet.iterrows()}

print([word_dict[_.upper()] for _ in input('Enter word: ')])
