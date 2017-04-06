import sys
from collections import Counter

def pick_number(a):
	c = Counter()
	for i in a:
	    c[i] += 1

	dic = dict(c)
	key = list(dic.keys())
	key.sort()
	count = 0
	if len(key)>1:
	    for i in range(0,len(key)-1):
	        if count<dic[key[i]]:
	            count = dic[key[i]]
	        if abs(key[i]-key[i+1]) <= 1:
	            if count < dic[key[i]] + dic[key[i+1]]:
	                count = dic[key[i]] + dic[key[i+1]]
	else:
	    count = dic[key[0]]
	print(count)


def main():
	n = int(input().strip())
	a = [int(a_temp) for a_temp in input().strip().split(' ')]

if __name__ == '__main__':
	main()






