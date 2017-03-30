def balance(prices,charged):
	if charged == (sum(prices)-prices[k])/2:
	    print("Bon Appetit")
	else:
	    print(int(charged - (sum(prices)-prices[k])/2))

def main():
	n,k = map (int,input().strip().split())
	prices = list(map (int,input().strip().split()))
	charged = int(input().strip())
	balance(prices,charged)

if __name__ == '__main__':
	main()