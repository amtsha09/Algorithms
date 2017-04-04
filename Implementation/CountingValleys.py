def main():
	n = int(input())
	steps = input()
	level = 0
	valley = 0

	for i in steps:
		if i == "U":
			level += 1
			if level == 0:
				valley += 1

		if i == "D":
			level -= 1

	print(valley)


if __name__ == '__main__':
	main()