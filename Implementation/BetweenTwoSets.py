from functools import reduce
import sys

def hcf(x,y):
    if y == 0:
        return x
    if y>x:
        return hcf(y,x)
    return hcf(y,x%y)


def find_hcf(b):
    return reduce(hcf,b)

def lcm(x,y):
    return x*y//hcf(x,y)

def find_lcm(a):
    return reduce(lcm,a)


if __name__ == "__main__":
    n,m = input().strip().split(' ')
    n,m = [int(n),int(m)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    b = [int(b_temp) for b_temp in input().strip().split(' ')]
    count = 0
    hcf_b = (find_hcf(b))
    lcm_a = (find_lcm(a))
    for i in range(lcm_a,hcf_b+1,lcm_a):
        if hcf_b % i == 0:
            count += 1
    print(count)