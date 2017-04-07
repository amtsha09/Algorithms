def main():

	n,k = input().strip().split(' ')
	n,k = [int(n),int(k)]
	height = list(map(int, input().strip().split(' ')))
	# your code goes here
	if max(height)<k:
	    print("0")
	else:
	    print(max(height)-k)

if __name__ == '__main__':
	main()