def main():
	h = list(map(int, input().strip().split(' ')))
	word = input().strip()
	print(max([h[ord(c)-ord('a')] for c in word]) * len(word))

if __name__ == '__main__':
	main()