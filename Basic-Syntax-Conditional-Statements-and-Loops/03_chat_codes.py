number_of_messages = int(input())
message = ''
for current_message in range(number_of_messages):
    number_code = int(input())
    if number_code == 88:
        message = 'Hello'
    elif number_code == 86:
        message = 'How are you?'
    elif number_code < 88:
        message = 'GREAT!'
    else:
        message = 'Bye.'
    print(message)
