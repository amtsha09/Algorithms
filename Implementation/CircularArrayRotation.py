def rotate(a):
	a.insert(0,a[-1])
	a.pop()
	return a

def main():
	n,k,q = input().strip().split(' ')
	n,k,q = [int(n),int(k),int(q)]
	a = [int(a_temp) for a_temp in input().strip().split(' ')]

	for i in range(k):
		rotate(a)

	for a0 in range(q):
		m = int(input().strip())
		print(a[m])

if __name__ == '__main__':
	main()