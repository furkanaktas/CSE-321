# http://www.cs.bilkent.edu.tr/~atat/473/lecture05.pdf  
# bu linkteki syf 5 ve 21 deki pseudo'lar  kullanılmıştır


def lomuto(arr, p, r): 
	pivot = arr[r]
	i = p-1	
	j = p

	while j < r:
		if arr[j] <= pivot:
			i = i+1
			arr[i],arr[j] = arr[j],arr[i]
		j = j+1
	
	arr[i+1],arr[r] = arr[r],arr[i+1] 		
	return i+1

			
def hoare(arr, p, r):
   
	pivot = arr[p]
	i = p - 1  # Initialize left index
	j = r + 1  # Initialize right index

	while True:
		
		# Find a value in right side smaller
		while True:
			j = j - 1
			if arr[j] <= pivot:
				break

		# Find a value in left side greater
		while True:
			i = i + 1
			if arr[i] >= pivot:
				break

		if i < j : 
			arr[i], arr[j] = arr[j], arr[i]
		else:	
			return j	  



def sortHoare(arr, p, r):

	if (p < r ) :
	    q = hoare(arr, p, r)
	    sortHoare(arr, p, q); 
	    sortHoare(arr, q + 1, r); 

	    

def sortLomuto(arr, p, r):

	if (p < r ) :
	    q = lomuto(arr, p, r)
	    sortLomuto(arr, p, q-1);  
	    sortLomuto(arr, q + 1, r); 


	    
def quickSortHoare(arr):
	temp = arr[:]
	sortHoare(temp, 0, (len(temp) - 1))	
	return temp


def quickSortLomuto(arr):
	temp = arr[:]
	sortLomuto(temp, 0, len(temp)-1)
	return temp





arr = [15,4,68,24,75,16,42]


qsh = quickSortHoare(arr)
print(qsh)

qsl = quickSortLomuto(arr)
print(qsl)
