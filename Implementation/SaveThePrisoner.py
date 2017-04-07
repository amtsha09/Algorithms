def main():
	T = int(input().strip())
	for i in range(T):
	    N,M,S = [int(a) for a in input().strip().split()]
	    
	    current = S-1
	    if current+M > N:
	        new = (current+M)%N
	        if new == 0:
	            print(N)
	        else:
	            print(new)
	    else:
	        print(current+M)


if __name__ == '__main__':
	main()