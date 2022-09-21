number = int(input())
largest_number = []
largest_integer = ''

for digit in str(number):
    for highest_digit in range(9, -1, -1):
        if int(digit) == highest_digit:
            largest_number.append(digit)
            break
largest_number.sort(reverse=True)
largest_integer = ''.join(largest_number)
print(int(largest_integer))