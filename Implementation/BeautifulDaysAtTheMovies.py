def rev(num):
    num = int(str(num)[::-1])
    return(num)

def main():
	i,j,k = [int(a) for a in input().strip().split()]

	count = 0
	
	for i in range(i,j+1):
	    if abs(i-rev(i))%k == 0:
	        count += 1
	
	print(count)

if __name__ == '__main__':
	main()
