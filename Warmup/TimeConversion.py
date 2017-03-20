import sys

def convert_time(time):
	hh,mm,ssSet = time.split(":")
	ss = ssSet[:2]
	Set = ssSet[2:]
	if hh == "12" and Set == "AM":
	    print("00:%s:%s"%(mm,ss))
	elif Set == "PM" and hh != "12":
	    print("%s:%s:%s"%(str(int(hh)+12),mm,ss))
	else:
	    print("%s:%s:%s"%(hh,mm,ss))



if __name__ == '__main__':
	time = input().strip()
	convert_time(time)
