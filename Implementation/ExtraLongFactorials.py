def main():

	n = int(input().strip())
	for i in range(1,n):
	    n *= i
	print(n)

if __name__ == '__main__':
	main()