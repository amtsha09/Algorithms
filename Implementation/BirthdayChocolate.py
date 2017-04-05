
import sys

def getWays(squares, d, m):
    count = 0
    if m<=len(squares):
        i = 0
        while i+m <= len(squares):
            if sum(squares[i:i+m]) == d :
                count += 1
            i += 1
        return count
    else:
        return 0
            
def main():
    n = int(input().strip())
    s = list(map(int, input().strip().split(' ')))
    d,m = input().strip().split(' ')
    d,m = [int(d),int(m)]
    result = getWays(s, d, m)
    print(result)    

if __name__ == '__main__':
    main()


