my_num = -2342

numbers_map = ["0", "1", "2", "3", "4",
               "5", "6", "7", "8", "9",
    ]

is_negative = False

if my_num == 0:
    print("0")
    exit()

if my_num < 0:
    my_num = abs(my_num)
    is_negative = True

number = my_num
str_number = ""

while number > 0:
    to_str = number % 10
    str_number = numbers_map[to_str] + str_number
    number //= 10

if is_negative:
    str_number = "-" + str_number

print(str_number)
print(type(str_number))