import sys

def main():
	dic = {}

	n = int(input().strip())
	types = list(map(int, input().strip().split(' ')))
	for t in types:
	    dic[t] = dic.get(t,0)+1
	print(sorted(dic.items(),key = lambda x: (-x[1],x[0]))[0][0])

if __name__ == '__main__':
	main()