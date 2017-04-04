import sys

def find_pairs(c):
	dic = {}
	for i in c:
	    dic[i] = dic.get(i,0)+1

	for i,j in dic.items():
	    dic[i] = j//2

	print(sum(dic.values()))



def main():
	n = int(input().strip())
	c = [int(c_temp) for c_temp in input().strip().split(' ')]
	find_pairs(c)



if __name__ == '__main__':
	main()

