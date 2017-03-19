
import sys

if __name__ == '__main__':
	
	a0,a1,a2 = input().strip().split(' ')
	a0,a1,a2 = [int(a0),int(a1),int(a2)]
	b0,b1,b2 = input().strip().split(' ')
	b0,b1,b2 = [int(b0),int(b1),int(b2)]
	alice = 0
	bob = 0
	for i in range(3):
	    if globals()["a%i"%i] > globals()["b%i"%i]:
	        alice += 1
	    elif globals()["a%i"%i] < globals()["b%i"%i]:
	        bob += 1

	print(alice, bob)