def my_str(num:int) -> str:
    numbers_map = [
        '0',
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]
    is_negative = False
    if num == 0:
        return "0"

    if num < 0:
        num = abs(num)
        is_negative = True

    number = num
    str_number = ""

    while number > 0:
        to_str = number % 10
        str_number = numbers_map[to_str] + str_number
        number //= 10

    if is_negative:
        str_number = "-" + str_number

    return str_number
print(my_str(10))
print(my_str(100))
print(my_str(-100))