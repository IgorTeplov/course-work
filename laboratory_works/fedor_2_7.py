from random import randint as r_int
from copy import copy

MIN = 0
MAX = 100

N = 10

array = [float(r_int(MIN, MAX)) for _ in range(N)]

def relocate_min_max(array):
    min_, max_ = min(array), max(array)
    count_min_, count_max_= array.count(min_), array.count(max_)

    new_min_array, new_max_array = copy(array), copy(array)

    for _ in range(count_min_):
        i = new_min_array.index(min_)
        new_min_array[i] = max_
        array[i] = max_

    for _ in range(count_max_):
        i = new_max_array.index(max_)
        new_max_array[i] = min_
        array[i] = min_

    print('COUNT MIN and MAX: ', count_min_, count_max_)

    return array

print('ARRAY: ', array)
print('MIN, MAX: ', min(array), max(array))

print('NEW ARRAY: ', relocate_min_max(array))