"""
son stün değişmeden kalır,  bu yüzden ilk for stün-1 kere çalışsa yeterli
2. for row sayısı kadar çalışır

ilk olarak sondan 1 önceki stün için değerler hesaplanır,  ilk stüna doğru ilerler.
her hesaplanan(col-2) stün'a, kendinden bir sonraki(col-1) stündaki,
çaprazlardaki(row ± 1) ve aynı row daki değerler arasında en büyük olan değer eklenir. (ilk ve son row için 1 tane çapraz var (row+1 veya row-1)) 


en son çöülen array deki en büyük eleman return edilir
"""

def theft(arr):
	col = len(arr[0])
	row = len(arr)

	temp = arr[:][:]

	
	for i in range(col-1):	
		for j in range(row):
			if j != 0 and j != row-1 : #ilk veya son satır değilse row'un kendisi, bir önceki ve bir sonraki rowlar arasındaki en büyük değerle toplanır
				
				ans = [temp[j-1][col-1-i], temp[j][col-1-i], temp[j+1][col-1-i]]
				index = (list(ans)).index(max(ans))   # en büyük değerin index'i 

				if index == 0:
					temp[j][col-2-i] += temp[j-1][col-1-i]
				elif index == 1:
					temp[j][col-2-i] += temp[j][col-1-i]
				else:
					temp[j][col-2-i] += temp[j+1][col-1-i]

			elif j == 0:	#ilk row ise kendisi ve bir sonraki row arasındaki en büyük değerle toplanır
				
				ans = [temp[j][col-1-i], temp[j+1][col-1-i]]
				index = (list(ans)).index(max(ans))    # en büyük değerin index'i 

				if index == 0:
					temp[j][col-2-i] += temp[j][col-1-i]
				else:
					temp[j][col-2-i] += temp[j+1][col-1-i]
			
			else:	# son row ise  kendisi ve bir önceki row arasındaki en büyük değerle toplanır
				
				ans = [temp[j][col-1-i], temp[j-1][col-1-i]]
				index = (list(ans)).index(max(ans))   # en büyük değerin index'i 

				if index == 0:
					temp[row-1][col-2-i] += temp[j][col-1-i]
				else:
					temp[row-1][col-2-i] += temp[j-1][col-1-i]


	
	result = []
	for i in range(row):	
		result.append(max(temp[i]))
										# sonuç array'in den en büyük değer return edilir
	return max(result)

	
amountOfMoneyInLand= [[1,3,1,5],
					  [2,2,4,1],
					  [5,0,2,3],
					  [0,6,1,2]]
res = theft(amountOfMoneyInLand)
print(res)
#Output: 16
amountOfMoneyInLand= [[10,33,13,15],
					  [22,21, 4, 1],
					  [5,  0, 2, 3],
					  [0,  6,14, 2]]
res = theft(amountOfMoneyInLand)
print(res)
#Output: 83