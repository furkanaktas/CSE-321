"""
findCommon(common1, common2)
bu fonksiyon gelen 2 string'in, sondaki ortak karakterlerini
return eder

common1 = longest_common_postfix(inpStrings[0:size2])
common2 = longest_common_postfix(inpStrings[size2:size])

yukarıdaki adımlar recursion olarak, 1 yada 2 string kalana kadar
devam eder, eğer 1 yada 2 tane kaldıysa return edilmeye başlar     			

return findCommon(common1, common2)


ilk satır sol taraf için,  2. satır sağ taraf için çalışır ve en son
bu 2 taraf tan gelen dönütte ortak karakterler return edilir. 

"""

def findCommon(inp1, inp2):
	
	size1 = len(inp1)
	size2 = len(inp2)

	size =0
	if(size1 < size2):
		size = size1    	# uzunluğu küçük olan size'a atanır 
	else:
		size = size2

	# sondaki karakterler eşit olduğu sürece common 'a eklenir
	common = ""
	for i in range(size):	# size kadar çalışır
		if ( inp1[size1-1-i] == inp2[size2-1-i] ):	
			common = inp1[size1-1-i] + common 

	return common


def longest_common_postfix(inpStrings):
	
	size = len(inpStrings)
	
	if(size == 0):
		return ""

	size2 = int(size/2)

	if( size <=2):
		if(size == 1):		# tek string varsa direk o return edilir
			return inpStrings[0]
		else: # değilse 2 tane vardır ve ortak karakterleri return eder
			return findCommon(inpStrings[0], inpStrings[1])	

	else:
		common1 = longest_common_postfix(inpStrings[0:size2])
		common2 = longest_common_postfix(inpStrings[size2:size])			
		return findCommon(common1, common2)




inpStrings = ["bash", "trash", "backslash", "flash"]

lcp = longest_common_postfix(inpStrings)
print(lcp)

inpStrings = ["absorptivity", "circularity", \
			 "electricity", "importunity", "humanity"]

lcp = longest_common_postfix(inpStrings)
print(lcp)

