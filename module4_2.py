a = [3, 8, 1, 23, 12, 9, 15]
def in_sort(a):
    for i in range(0, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a
print(a)
in_sort(a)
print(in_sort(a))
