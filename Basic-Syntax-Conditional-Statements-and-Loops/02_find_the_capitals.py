current_string = input()
capital_letters_list = []
index_counter = 0

for letter in current_string:
    if letter.isupper():
        capital_letters_list.append(index_counter)
        index_counter += 1
    else:
        index_counter += 1
        continue
print(capital_letters_list)