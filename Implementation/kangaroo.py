import sys

def kangaroo(x1,x2,v1,v2):
    while True:
    if x1>x2 :
        if v1 >= v2:
            print("NO")
            break
    elif x2>x1:
        if v2>=v1:
            print("NO")
            break
    elif x1 == x2:
        print("YES")
        break
    x1 += v1
    x2 += v2

if __name__ == "__main__":
    x1,v1,x2,v2 = input().strip().split(' ')
    x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
    kangaroo(x1,x2,v1,v2)