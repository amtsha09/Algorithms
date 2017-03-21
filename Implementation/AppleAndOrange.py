import sys

def count_fruit(a,b,s,t,m,n,apple,orange):
	app_count = 0
	org_count = 0
	for app in apple:
	    if a+app >= s and a+app <= t:
	        app_count += 1

	for org in orange:
	    if b+org >= s and b+org <= t:
	        org_count += 1
	        
	print(app_count)
	print(org_count)



if __name__ == '__main__':
	s,t = input().strip().split(' ')
	s,t = [int(s),int(t)]
	a,b = input().strip().split(' ')
	a,b = [int(a),int(b)]
	m,n = input().strip().split(' ')
	m,n = [int(m),int(n)]
	apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
	orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
	count_fruit(a,b,s,t,m,n,apple,orange)