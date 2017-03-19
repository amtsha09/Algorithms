import sys

def digonal_difference(a,n):
    sd=0
    pd=0
    for i in range(n):
        sd += a[i][-1-i]
        pd += a[i][i]
    return(abs(pd-sd))
    
    
    
if __name__ == "__main__":
    
    n = int(input().strip())
    a = []
    for a_i in range(n):
        a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
        a.append(a_t)
        
    print(digonal_difference(a,n))