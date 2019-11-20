# -*- encoding: utf-8 -*-
import csv

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

            meibo_ids = [m[0] for m in meibo]
            try:
                found_at = meibo_ids.index(id)
                meibo[found_at][1] = name
                print(id, "番の情報を更新しました")
            except ValueError:
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
        # import を行った場合、既存のデータは消去されることにする
        if len(params) == 1:
            filename = params[0]

            # 改行文字対策で newline オプションを指定
            with open(filename, mode="r", newline='') as file_obj:
                csv_reader = csv.reader(file_obj)
                meibo = [r for r in csv_reader]

    elif command == 'export':
        if len(params) == 1:
            filename = params[0]

            # 改行文字対策で newline オプションを指定
            with open(filename, mode="w", newline='') as file_obj:
                csv_writer = csv.writer(file_obj)
                csv_writer.writerows(meibo)
    else:
        print('input command')
         
