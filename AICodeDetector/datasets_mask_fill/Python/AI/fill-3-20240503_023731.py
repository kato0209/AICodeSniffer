def sequential_search(arr, target):
    for index, element in enumerate(arr):
       if element == target:
           return index  # 目的の要素が見つかった場合、そのインデックスを返す
    return None  # テストコード
if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    print(sequential_search(my_list, 11)) # 出力: 5
    print(sequential_search(my_list, 15))  # 出力: None
