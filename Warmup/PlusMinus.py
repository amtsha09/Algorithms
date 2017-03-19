
import sys
def plus_minus(arr):
    pos = 0
    neg = 0
    zero = 0
    for a in arr:
        if a > 0:
            pos += 1
        elif a < 0 :
            neg += 1
        else:
            zero += 1

    print("%.6f"%(pos/n))
    print("%.6f"%(neg/n))
    print("%.6f"%(zero/n))

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
plus_minus(arr)