# http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
# permutasyon için yararlanıldı


def permute(array, start, end, permutatedArray):
	if start==end:
		permutatedArray.append(array[:])
	else:
		for i in range(start,end+1):
		    array[start], array[i] = array[i], array[start]
		    permute(array, start+1, end, permutatedArray)
		    array[start], array[i] = array[i], array[start] # backtrack


def findOptimalAssistantship(inputTable):

	numberOfRa = len(inputTable)		# number of assistants
	numberOfCourse = len(inputTable[0])	# number of courses


	if ( numberOfRa >= numberOfCourse):

		course = list(range(numberOfCourse)) 	# kurs indexlerini içeren array (3 ders varsa 0 1 2)
		ra = list(range(numberOfRa))			# assist. indexlerini içeren array (3 asist. varsa 0 1 2)

		perRa = []		# assit. permutasyonları
		perCourse = []	# derslerin permutasyonları

		permute(ra, 0, numberOfRa-1, perRa)
		permute(course, 0, numberOfCourse-1, perCourse)

		sizeRa = len(perRa)			# assist.   toplam permutasyon sayısı
		sizeCourse = len(perCourse)	# kursların toplam permutasyon sayısı

		
		minTime = float("inf")		#infinite
		temp =0						#minTime değeri için
		resultR,resultN =  [], []	#bulunan en küçük minTime için doğru indexler
		
		for i in range(sizeRa):
			for j in range(sizeCourse):
				temp =0
				tempR, tempN = [], []
				
				for k in range(numberOfCourse):
					temp += inputTable[ perRa[i][k] ][ perCourse[j][k] ]
					tempR.append(perRa[i][k])
					tempN.append(perCourse[j][k])

				if (minTime > temp):
					resultR, resultN = tempR, tempN # minTime durumundaki assit-kurs eşleşmeleri atandı.
					minTime = temp	


		result = []		# resultR ve resultN nin birleşimi (ödevde istenilen return)

		for i in range(numberOfRa):			# assist. sayısı kadar , her biri -1
			result.append(-1)
				

		for i in range(len(resultR)):		# minTime durumundaki assit-kurs eşleşmeleri result'a atandı.
			result[resultR[i]] = resultN[i]

		for i in range(len(result)):		# boştaki her assit. için 6 saat eklendi
			if (result[i] == -1):
				minTime += 6

		return result , minTime	
	
	else:
		print ("It should be always R >= N")
		return [], 0		



inputTable = [	[5, 8,  7],
				[8, 12, 7],
				[4, 8,  5]]


inputTable2 = [	[8, 12, 7],
			  	[5, 8,  7],
			  	[4, 8,  5],
			  	[8, 12, 7],
			  	[4, 8,  5]]



asst, time = findOptimalAssistantship(inputTable)
print(asst)
print(time)

asst, time = findOptimalAssistantship(inputTable2)
print(asst)
print(time)