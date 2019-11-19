# -*- encoding: utf-8 -*-
meibo = []

while True:
    raw_input_text = input('command > ')
    splited_input = raw_input_text.split(' ')
    command, params = splited_input[0], splited_input[1:]

    if command == 'exit':
        quit(0)
    elif command == 'set':
        if len(params) == 2:
            id = params[0]
            name = params[1]

            meibo.append([id, name])
            print("ユーザを追加しました", id)
    elif command == 'get':
        pass
    elif command == 'import':
        pass
    elif command == 'export':
        pass
    else:
        print('input command')
         
