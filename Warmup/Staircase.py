def staircase(n):
    for i in range(n-1,-1,-1):
        print(" "*i,"#"*(n-i),sep="")

if __name__ == "__main__":
    
    n = int(input().strip())
    staircase(n)