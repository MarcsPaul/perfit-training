def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = int(len(arr)/2)
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


def merge(l_half, r_half):
    res = []
    while len(l_half) != 0 and len(r_half) != 0:
        if l_half[0] < r_half[0]:
            res.append(l_half[0])
            l_half.remove(l_half[0])
        else:
            res.append(r_half[0])
            r_half.remove(r_half[0])
    if len(l_half) == 0:
        res = res + r_half
    else:
        res = res + l_half
    return res


arr = []
lim = int(input("Enter the limit"))
for i in range(0, lim):
    eleme = int(input("Enter the values"))
    arr.append(eleme)
lngth = len(arr)
print(merge_sort(arr))
