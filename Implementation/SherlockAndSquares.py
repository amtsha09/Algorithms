import math

def main():
	n = int(input().strip())
	for i in range(n):
	    a,b = [int(x) for x in input().strip().split()]
	    count = math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1
	    print(count)

if __name__ == '__main__':
	main()