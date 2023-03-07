a = [3, 8, 1, 23, 12, 9, 15]
def in_sort(a):
    res = []
    for i in range(1, len(a)):
        key = a[i]
        j = i
        while (j - 1 >= 0) and (a[j - 1] > key):
            a[j - 1], a[j] = a[j], a[j - 1]
            j = j - 1
            a[j] = key
            res.append(a)
            return res
print(a)
print(in_sort(a))
