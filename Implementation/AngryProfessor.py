def main():

	t = int(input().strip())
	for a0 in range(t):
	    n,k = input().strip().split(' ')
	    n,k = [int(n),int(k)]
	    a = [int(a_temp) for a_temp in input().strip().split(' ')]
	    a = [True if a_temp<=0 else False for a_temp in a]
	    if sum(a) >= k:
	        print("NO")
	    else:
	        print("YES")

if __name__ == '__main__':
	main()