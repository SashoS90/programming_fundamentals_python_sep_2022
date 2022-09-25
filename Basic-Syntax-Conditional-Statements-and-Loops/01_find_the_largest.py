# Input.
number = int(input())

# Empy list to add all the digits of the received integer.
largest_number = []

# Empty string for forming the final output of the output.
largest_integer = ''

# For loop through the string of the received input to find and add the highest digits into the largest number list.
for digit in str(number):
    for highest_digit in range(9, -1, -1):
        if int(digit) == highest_digit:
            largest_number.append(digit)
            break

# Sorting the largest number list from highest to lowest numbers.
largest_number.sort(reverse=True)

# Joining the separate elements in the list to form the final output.
largest_integer = ''.join(largest_number)

# Final output.
print(int(largest_integer))
