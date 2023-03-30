def custom_filter(some_list: list) -> bool:
    s: int = 0
    for i in some_list:
        if type(i) is int:
            if i%7 == 0: s+=i
    return not s > 83

some_list = [7, 14, 28, 32, 32, 56]

print(custom_filter(some_list))
