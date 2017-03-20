import sys
def grading(grade):
    if grade >= 38:
        if grade%5 >= 3:
            print(grade+(5-(grade%5)))
        else:
            print(grade)
    else:
        print(grade)


if __name__ == "__main__":
    n = int(input().strip())
    for a0 in range(n):
        grade = int(input().strip())
        grading(grade)