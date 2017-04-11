def main():
	t = int(input().strip())
	for a0 in range(t):
	    count = 0
	    n = int(input().strip())
	    for i in str(n):
	        if int(i) != 0 and n%int(i) ==0:
	            count += 1
	    print(count)

if __name__ == '__main__':
	main()