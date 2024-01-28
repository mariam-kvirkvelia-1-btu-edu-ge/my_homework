#1. დაწერე კოდი რომელიც article.txt _დოკუმენტში იპოვის რიგით მეორე ყველაზე ხშირად განმეორებად სიტყვას.
from collections import Counter
def find_second_most_common_word(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        word_count = Counter(words)
        # Find the second most common word using Counter's most_common method
        second_most_common = word_count.most_common(2)[-1]
        return second_most_common[0] if second_most_common else "There's no second most common word."

second_most_common_word = find_second_most_common_word('article.txt')
print("Second most frequently repeated word:", second_most_common_word)

#2. names.csv ფაილში არსებული ინფორმაცია გადმოაკოპირე names.txt ფაილში.

def copy_csv_to_txt(csv_filename, txt_filename):
    with open(csv_filename, 'r') as csv_file:
        with open(txt_filename, 'w') as txt_file:
            for line in csv_file:
                txt_file.write(line)

copy_csv_to_txt('names.csv', 'names.txt')
print("Names copied from names.csv to names.txt")