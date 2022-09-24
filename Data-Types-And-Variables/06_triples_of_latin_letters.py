number_of_symbols = int(input())
combinations = ()

for first_char in range(97, 97 + number_of_symbols):
    for second_char in range(97, 97 + number_of_symbols):
        for third_char in range(97, 97 + number_of_symbols):
            print(f"{chr(first_char)}{chr(second_char)}{chr(third_char)}")
