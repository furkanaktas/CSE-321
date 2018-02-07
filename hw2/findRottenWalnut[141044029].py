
def compareScales (leftScaleList, rightScaleList):
	result = sum(leftScaleList) - sum(rightScaleList)
	if result < 0:
		return 1
	elif result > 0:
		return -1
	else:
		return 0

def findRottenWalnut(nutList):
	
	size = len(nutList)
	if(size <= 1):
		return None;

	sizeLeft  = int(size/2)
	sizeRight = size - sizeLeft
	
	left = nutList[0:sizeLeft]
	right = nutList[sizeLeft:size]

	#print (nutList, "\n",left ,"     ", right,"\n\n")

	if(size >3):
		if(compareScales(left, right) == 0):
			return None;

		if (sizeLeft == sizeRight):

			if(compareScales(left, right) == 1  ):
				return findRottenWalnut(left);

			elif(compareScales(left, right) == -1 ):
				return findRottenWalnut(right) + sizeLeft;	


		else:
			if( findRottenWalnut(left) == None):
				return findRottenWalnut(right) + sizeLeft;
			else:
				return findRottenWalnut(left);

	else:
		if(size ==2):
			if (left[0] == right[0]):
				return None;
			elif (left[0] < right[0]):
				return 0;	
			else:
				return 1;	

		elif(size == 3):
			if( (left[0] == right[0]) and (left[0] == right[1]) ):
				return None;
			elif(left[0] == right[1]):
				return 1;	
			elif(left[0] == right[0]):
				return 2;
			else:	
				return 0;	 


listEx = [ 1,1,1,1,1,0.5,1,1,1 ];		

print ("Index  : ", findRottenWalnut(listEx))
