
import sys

def win(x,y,z):
    if abs(x-z)<abs(y-z):
        print("Cat A")
    elif abs(y-z)<abs(x-z):
        print("Cat B")
    else:
        print("Mouse C")
        
def main():
	q = int(input().strip())

	for a0 in range(q):
	    x,y,z = input().strip().split(' ')
	    x,y,z = [int(x),int(y),int(z)]
	    win(x,y,z)

if __name__ == '__main__':
	main()

