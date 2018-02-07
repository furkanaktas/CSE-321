"""
i index'i  1 yapılacak indextir.

başlangıç hariç diğer durumlarda  i 1 olsa ne olur  ve i+1  1 olsa ne olur'a  bakılır.
i 1 olduğundaki durum büyükse i+=2, i i+1 deki büyükse  i+=3 olur
Y = [79, 6, 40,....] örneğin burada [79, 1, 40,...] olur, yani 1 olanın sağı ve solu artık 1 yapılamaz bu yüzden +2 artırılır
i+1  1 yapıldığında ise +1 daha eklenir yani +3  artırılır

"""
def find_maximum_cost(arr):
	x = arr[:]
	
	start = 0
	if  abs(x[0]-1) + abs(x[2]-1) > abs(x[1]-1) + abs(x[1]- x[2]) :
		x[1]  = 1			# ilk eleman 1 olduğunda yada, 2. eleman 1 olduğunda elde edilen toplamlardan büyük olana göre
		start = 1			# Y = [79, 6, 40, 68, 68, 16, 40, 63, 93, 49, 91] burada [79,1,40....] olur
	else:
		x[0] = 1			# Y = [50,28,1,1,13,7] örnek burada  [1,28,1... ] olur 
	
	i= start +2  		# i index'i  1 yapılacak olan indextir ve 1 yapılan index'in sağında veya solundaki sayı 1 yapılmaz
	while i< len(arr) :
		if abs(x[i-1] -1)+ abs(x[i+1] -1) > abs(x[i]- x[i-1])+ abs(x[i]-1):  # i  1'ken toplam > i+1  1'ken toplam 		
			x[i] = 1	# i 1 olursa                                     -1 ler, 1 yapılıcak index olarak varsayılıyor
			i += 2
		else:
			x[i+1]= 1	# i+1 1 olursa,  bazen i+1 1 yapıldığında daha büyük toplam elde edilir 
			i += 3

		if i == len(arr)-1:		# i değiştiğinde son elemana geldiysek, son elemanı 1 yapıyoruz
			x[i] = 1			# Y = [50,28,1,1,13,7] örneğin burada i son elemana(7) denk gelir, yani ...,13, 1] şeklinde sonlanır
			i += 1					

	#print(x)
	
	result = 0
	i = 1
	while i < len(arr):
		result += abs(x[i] - x[i-1])  # array belirlendikten sonra maximum cost bulunur 
		i += 1 						  

	return result



Y = [14,1,14,1,14]
cost = find_maximum_cost(Y)
print(cost)
#Output: 52

Y = [1,9,11,7,3]
cost = find_maximum_cost(Y)
print(cost)
#Output: 28

Y = [50,28,1,1,13,7]
cost = find_maximum_cost(Y)
print(cost)
#Output: 78

Y = [80, 22, 45, 11, 67, 67, 74, 91, 4, 35, 34, 65, 80, 21, 95, 1, 52, 25, 31, 2, 53]
cost = find_maximum_cost(Y)
print(cost)
#Output: 1107

Y = [79, 6, 40, 68, 68, 16, 40, 63, 93, 49, 91]
cost = find_maximum_cost(Y)
print(cost)
#Output: 642

Y = [1,9,111,7,3] 
cost = find_maximum_cost(Y)
print(cost)
#Output: 222
