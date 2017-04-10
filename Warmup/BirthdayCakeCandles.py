def main():
	n = int(input().strip())
	height = [int(height_temp) for height_temp in input().strip().split(' ')]
	print (height.count(max(height)))

if __name__ == '__main__':
	main()