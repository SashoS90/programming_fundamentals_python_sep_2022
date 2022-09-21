budget = int(input())
command = input()

while command != 'End':
    spending = int(command)
    if spending > budget:
        print(f"You went in overdraft!")
        break
    budget -= spending
    command = input()
if command == 'End':
    print(f"You bought everything needed.")