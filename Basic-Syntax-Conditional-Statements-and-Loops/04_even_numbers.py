number_of_lines = int(input())

for number in range(number_of_lines):
    current_number = int(input())
    if current_number % 2 != 0:
        print(f"{current_number} is odd!")
        break
else:
    print(f"All numbers are even.")