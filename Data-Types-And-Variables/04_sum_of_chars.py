characters_number = int(input())
sum_of_characters = 0

for character in range(characters_number):
    current_character = input()
    sum_of_characters += ord(current_character)
print(f"The sum equals: {sum_of_characters}")