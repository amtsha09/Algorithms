import sys

def main():
	n = int(input().strip())
	score = list(map(int, input().strip().split(' ')))
	mi = ma = score[0]
	count_min = 0
	count_max = 0
	for s in score:
	    if s < mi:
	        mi = s
	        count_min += 1
	    if s > ma:
	        ma = s
	        count_max += 1
	print(count_max, count_min)


if __name__ == '__main__':
	main()