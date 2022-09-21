command = input()
coffees_needed = 0

while command != 'END':
    if command.isupper():
        command = command.lower()
        if command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
            coffees_needed += 2
    elif command.islower():
        if command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
            coffees_needed += 1
    else:
        command = input()
        continue
    command = input()
if coffees_needed <= 5:
    print(coffees_needed)
else:
    print(f"You need extra sleep")