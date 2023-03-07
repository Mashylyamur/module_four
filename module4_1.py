a = [56, 4, 9, 5, 3, 11]
x = int(input('Введите число из массива: '))
a1 = sorted(a)
def binar_search(a1, x):
    low = 0
    high = len(a1) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if a1[middle] == x:
            return middle
        elif a1[middle] < x:
            low = middle + 1
        else:
            high = middle - 1
print(a)
print(a1)
print(binar_search(a1, x))