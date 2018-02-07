"""
girilen sayı < 3 ise return -1
önce verilen değer için hepsi 5 oluyor mu ona bakılır.
sonra en az miktardaki 3 (5 ve 5'in katları sayıda olmak zorunda) ve 5'ler için bakılır.
hiç biri olmazsa en son hepsinin 3 olması durumuna bakılır.
oda olmazsa return -1 
"""

"""
fives 5 ler toplamının 3 e bölünüyorsa sayıyı return eder
"""
def fives(num):
	sum_num = 0
	result = 0
	for i in range(num):
		sum_num += 5
		result += (10**i)*5
	
	if sum_num % 3 == 0:
		return result
	else:
		return 0	

"""
threes 3 ler toplamının 5 e bölünüyorsa sayıyı return eder
"""
def threes(num):
	sum_num = 0
	result = 0
	for i in range(num):
		sum_num += 3
		result += (10**i)*3
	
	if sum_num % 5 == 0:
		return result
	else:
		return 0			 			


def decentNumber(num):
	if num < 3:
		return -1

	else:
		result = fives(num)
		if result != 0:
			return result		# hepsi 5 olabiliyorsa 

			
		#karışık sayılar için
		three = 5    # en az 5 tane 3 gerekli, 5'e bölünmesi için 
		while three <= num:
			res_three = threes(three)	 
			res_five = fives(num-three)	# sayının kalanı 5 olursa
										# 3'e bölünüyor mu
			if res_three != 0 and res_five != 0:
				return res_five*(10**three) + res_three  
			
			three += 5 # 5'e bölünme için 
					   # 3'ten 5'in katı sayıda olması lazım
			
		
		result = threes(num)
		if result != 0:
			return result	# hepsi 3 olabiliyorsa 
		
		return -1		# hiç biri değilse return -1




for i in range(0,100):
    dn = decentNumber(i)
    print(i,dn)


