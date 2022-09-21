command = input()
while command != 'Welcome!':
    student_name = str(command)
    if student_name == 'Voldemort':
        break
    if len(student_name) < 5:
        print(f"{student_name} goes to Gryffindor.")
    elif len(student_name) == 5:
        print(f"{student_name} goes to Slytherin.")
    elif len(student_name) == 6:
        print(f"{student_name} goes to Ravenclaw.")
    elif len(student_name) > 6:
        print(f"{student_name} goes to Hufflepuff.")
    command = input()
if command == 'Voldemort':
    print(f"You must not speak of that name!")
else:
    print(f"Welcome to Hogwarts.")
