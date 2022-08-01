import matplotlib.pyplot as plt
from numpy import number


def ranked_series(arr):
    return list(sorted(arr))

def variation_series(arr):
    return list(sorted(set(arr)))

def freq_series(arr):
    return [arr.count(el) for el in variation_series(arr)]

def rel_freq_series(arr):
    return [round(c/len(arr), 3) for c in freq_series(arr)]

def table_freq_series(arr):
    vs = variation_series(arr)
    rel_freqs = rel_freq_series(arr)
    return {v: r for v, r in zip(vs, rel_freqs)}

def scope_series(arr):
    var = variation_series(arr)
    return abs(var[0] - var[-1])

def moda_series(arr):
    table = table_freq_series(arr)
    keys = list(table.keys())
    values = list(table.values())
    index_maxv = values.index(max(values))
    return keys[index_maxv]
     
def median_series(arr):
    rs = ranked_series(arr)
    lrs = len(rs)

    if lrs%2:
        result = rs[int(lrs/2)]
    else:
        lft = rs[int(lrs/2)]
        rgt = rs[int(lrs/2) + 1]
        result = (lft + rgt) / 2
    return result

def interval_series(arr):
    k = 5
    li = scope_series(arr)/k
    iv = [min(arr)]
    numbers = []
    for i in range(k-1):
        iv.append(iv[-1]+li)
        nums = []
        for num in arr:
            if iv[i] <= num < iv[-1]:
                nums.append(num)
        numbers.append(nums)
    iv.append(iv[-1]+li)
    numbers.append([el for el in arr if el >= iv[-1]])
    return {i: n for i, n in zip(iv, numbers)}


def interval_freq_series(arr):
    table = interval_series(arr)
    keys = list(table.keys())
    values = list(table.values())
    return {iv: len(val) for iv, val in zip(keys, values)}

def rel_interval_freq_series(arr):
    table = interval_series(arr)
    keys = list(table.keys())
    values = list(table.values())
    return {iv: len(val)/len(arr) for iv, val in zip(keys, values)}
