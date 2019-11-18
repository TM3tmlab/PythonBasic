# -*- encoding: utf-8 -*-
meibo = []

while True:
    raw_input_text = input('command > ')
    splited_input = raw_input_text.split(' ')
    command, params = splited_input[0], splited_input[1:]

    if command == 'exit':
        quit(0)
    elif command == 'set':
        pass
    elif command == 'get':
        pass
    elif command == 'import':
        pass
    elif command == 'export':
        pass
    else:
        print('input command')
         
