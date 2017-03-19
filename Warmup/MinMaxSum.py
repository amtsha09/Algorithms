import sys

if __name__ == '__main__':	
	a,b,c,d,e = input().strip().split(' ')
	a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
	print(sum(sorted([a,b,c,d,e],reverse=False)[:4]),sum(sorted([a,b,c,d,e],reverse=True)[:4]))