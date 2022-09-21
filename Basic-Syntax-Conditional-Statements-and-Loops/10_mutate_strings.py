first_string = input()
second_string = input()
final_string = ''
previous_string = ''
n = 1

for i in range(len(first_string)):
    final_string += second_string[:n] + first_string[n:]
    n += 1
    if final_string != previous_string and final_string != first_string:
        print(final_string)
    previous_string = final_string
    final_string = ''
