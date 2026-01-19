
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
user_input = input("Enter array elements separated by space: ")
user_input = user_input.split()
arr = list(map(float, user_input))
arr = bubble_sort(arr)
print(arr)