import sys

def main():
	n = int(input().strip())
	p = int(input().strip())
	count_min_page(n,p)

def count_min_page(n,p):
	count = 0

	for i in range(0,n//2):
	    count = i
	    if p==(2*i) or p==(2*i)+1:
	        break
	    if n%2 == 0:
	        if p==(n-(2*i)) or p==(n-(2*i)+1):
	            break
	    else:    
	        if p==(n-(2*i)) or p==(n-(2*i)-1):
	            break

	print(count)



if __name__ == '__main__':
	main()




