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

            # meibo は リスト の中に リスト が入っている2次元構造のため、
            # 1次元リストから検索を行う index メソッドをそのまま使えない。
            # そのため、2次元リストの id を表す場所だけを抽出した新しい1次元リストを
            # 作成している。
            
            # [] の中に for が書かれているが、このような記述を リスト内包表現 という
            # 次のようなコードと 等価 となっている
            # meibo_ids = []
            # for m in meibo:
            #   meibo_ids.append(m[0])
            meibo_ids = [m[0] for m in meibo]

            # index は検索している値が見つからなかった場合 ValueError という 例外 を発生させる
            # 例外が発生するとき、何も対処をしなければプログラムが止まるようになっている。
            # 今回は見つからなかった場合の 挙動(ムーブ、動作、動き) は決まっているので
            # 例外を制御する構文 try-except を使って見つからなかった場合の挙動を実装している
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
         
