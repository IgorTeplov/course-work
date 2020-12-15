from random import randint as r_int

MIN = 0
MAX = 100

N = 10

array = [float(r_int(MIN, MAX)) for _ in range(N)]

def sum_for_min(array):
    if array.index(min(array)) == 0:
        return 0
    slice_for_min = array[:array.index(min(array))]

    return sum(slice_for_min)

print('ARRAY: ', array)
print('index, MIN: ', array.index(min(array)), min(array))

print('SUM FOR MIN IN ARRAY: ', sum_for_min(array))