def main():
	n,k = input().strip().split(' ')
	n,k = [int(n),int(k)]
	c = [int(c_temp) for c_temp in input().strip().split(' ')]
	energy = 100
	for i in range(0,n,k):
		if c[i] == 0:
			energy -= 1
		elif c[i] == 1:
			energy -= 3
	print(energy)

if __name__ == '__main__':
	main()