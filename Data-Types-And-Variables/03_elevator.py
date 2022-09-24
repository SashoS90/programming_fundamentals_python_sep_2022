from math import ceil

number_of_persons = int(input())
capacity = int(input())
courses_needed = number_of_persons / capacity
print(ceil(courses_needed))