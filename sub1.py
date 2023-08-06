def ave(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    ave = sum / len(a)
    return ave
