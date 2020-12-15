from random import randint as r_int

MIN = 0
MAX = 100

N = 100

array = [r_int(MIN, MAX) for _ in range(N)]
array.sort()

def InterpolationSearch(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low+int(((float(high - low)/(lys[high]-lys[low]))*(val-lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return -1

print('ARRAY: ', array)
print('POSITION of number "10"(-1 this array don\'t have "10"): ', InterpolationSearch(array, 10))