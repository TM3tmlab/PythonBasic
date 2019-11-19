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
        if len(params) == 1:
            id = params[0]

            meibo_ids = [m[0] for m in meibo]
            try:
                found_at = meibo_ids.index(id)
                print(id, "番は", meibo[found_at][1], "さんです")
            except ValueError:
                print(id, "は登録されていません")

    elif command == 'import':
        pass
    elif command == 'export':
        pass
    else:
        print('input command')
         
