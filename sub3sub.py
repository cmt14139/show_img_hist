def Max(a):
    max = a[0]
    for i in range(len(a)):
        if max < a[i]:
            max = a[i]
    return max


def Min(a):
    min = a[0]
    for i in range(len(a)):
        if min > a[i]:
            min = a[i]
    return min
