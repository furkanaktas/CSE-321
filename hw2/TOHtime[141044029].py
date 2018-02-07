import math 

def moveTower(A, B, C, n):
	if n == 1:
		printMove(A,C,n)
		d = distance(A, C)
		time[n-1] += d*n
	else:
		moveTower(A, C, B, n-1)
		printMove(A, C, n)
		d = distance(A, C)
		time[n-1] += d*n
		moveTower(B, A, C, n-1)    


def printMove(fp,tp,n):
	print("disk " ,n, ": ",fp," to ",tp, sep='')


def distance(src, dest):
	x=0
	y=0
	if src == "SRC":
		x=0
	elif src == "AUX":
		x=1
	elif src == "DST":
		x=2	
	
	if dest == "SRC":
		y=0
	elif dest == "AUX":
		y=1
	elif dest == "DST":
		y=2

	return int(math.fabs(y-x));			


plate = int(input("Enter plate number: "))
time = [0] * plate
moveTower("SRC", "AUX", "DST", plate)

for i in range(plate):
	print("Elapsed time for disk ", i+1, ": ",time[i])


