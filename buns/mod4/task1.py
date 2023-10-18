def task1(data):
    data_len = len(data)
    data_set_len = len(set(data))
    if data_len == data_set_len:
        return "Все числа разные"
    elif data_set_len == 1:
        return "Все числа равны"
    else:
        return "Есть равные и неравные числа"


print(task1(input().split()))
