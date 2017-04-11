def main():
	s = input().strip()
	t = input().strip()
	k = int(input().strip())
	for i in range(min(len(s),len(t))):
	    if s[i] != t[i]:
	        break
	    
	if ((len(s)+len(t)-2*i <= k) and ((len(s)+len(t)-2*i)%2 == k%2)) or (len(s)+len(t) < k):
	    print("Yes")
	else:
	    print("No")

if __name__ == '__main__':
	main()