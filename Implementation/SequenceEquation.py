def main():
	n = int(input().strip())
	a = [int(temp) for temp in input().strip().split()]
	dic = {}
	for ind,i in enumerate(a):
		dic[i] = ind+1

	for i in range(1,len(a)+1):
		print(dic[dic[i]])

if __name__ == '__main__':
	main()