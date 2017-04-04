


def print_cost(pendrives,keyboards):
	min = 0
	for pen in pendrives:
	    for ke in keyboards:
	        if pen+ke >= min and pen+ke<=s:
	            min = pen+ke
	if min == 0:
	    print("-1")
	else:
	    print(min)	


def main():
	s,n,m = input().strip().split(' ')
	s,n,m = [int(s),int(n),int(m)]
	keyboards = [int(keyboards_temp) for keyboards_temp in input().strip().split(' ')]
	pendrives = [int(pendrives_temp) for pendrives_temp in input().strip().split(' ')]
	print_cost(pendrives,keyboards)

	

if __name__ == '__main__':
	main()


