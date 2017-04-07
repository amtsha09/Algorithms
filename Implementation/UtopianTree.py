def main():
	t = int(input().strip())

	for a0 in range(t):
	    n = int(input().strip())
	    height = 1
	    if n!=0:
	        for i in range(n):
	            if i%2 == 0:
	                height *= 2
	            else:
	                height += 1
	    print(height)

if __name__ == '__main__':
	main()