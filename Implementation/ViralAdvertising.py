def count_person(n):
	count = 0
	person = 5
	for i in range(1,n+1):
	    count += person//2
	    person = (person//2)*3

	print(count)


def main():
	n = int(input().strip())
	count_person(n)

if __name__ == '__main__':
	main()