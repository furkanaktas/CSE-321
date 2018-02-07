"""
minSubArr fonksiyonu array, başlangıç bitiş index'ini alır

ve hangi eleman en küçükse, onun değeri, aralığı ve sub array'i 
return edilir 

leftSum, temp, l1, h1  = minSubArr(arr, l, m)
rightSum, temp, l2, h2  = minSubArr(arr, m+1, h )
midSum, l3, h3   = midSum(arr, l, m, h)

bu satırlarda sol taraf için, sağ taraf için, orta değer için en küçük
bulunur bu aşamada önemli olan  sayı değerleridir.Bu satırlar 
recursion olarak başlangıç ve bitiş eşit olana kadar tekrarlar.

ans = [leftSum, rightSum, midSum]
index = (list(ans)).index(min(ans))   # en küçük değerin index'i

daha sonra bu satırlarla en küçük olanın index'i bulunur.
ve hangi index en küçükse, onun değeri, aralığı ve sub array'i 
return edilir 
  if index == 0:
    return leftSum, arr[l1:h1+1], l1, h1
  elif index == 1:
    return rightSum, arr[l2:h2+1], l2, h2
  else:
    return midSum, arr[l3:(h3+1)], l3, h3

recursion ilk başladığı duruma yani

leftSum, temp, l1, h1  = minSubArr(arr, l, m)
rightSum, temp, l2, h2  = minSubArr(arr, m+1, h )
midSum, l3, h3   = midSum(arr, l, m, h)

buranın sonuna geldiğinde  en küçük olan sub array çağrıldığı yere
return edilmiş olur    

"""

import sys  #sys.maxsize  için

# sağ ve sol daki elemanlar toplamı ve , 
# en küçük toplam array aralığı (l1, h1) return eder
def midTotal(arr, l, m, h):

  # Array'in sol tarafını toplam daha küçük oldukça değişkende tutar
  sum = 0
  left_sum = sys.maxsize
  i = m

  l1 = m    # en son toplanan index'i belirtir 
  while i >= l:
    sum = sum + arr[i]
    if (sum < left_sum):
      left_sum = sum
      l1 = i    # en son toplanan index'i belirtir (toplamı en küçük) 
    i -= 1

  # Array'in sağ tarafını toplam daha küçük oldukça değişkende tutar
  sum = 0;
  right_sum = sys.maxsize
  i = m+1

  h1 =m+1   # en son toplanan index'i belirtir
  while i <= h:
    sum = sum + arr[i]
    if (sum < right_sum):
      right_sum = sum
      h1 = i      # en son toplanan index'i belirtir
    i += 1

  # sağ ve sol daki elemanlar toplamı ve , 
  # en küçük toplam array aralığı (l1, h1) return edilir
  return (left_sum + right_sum), l1, h1


# en küçük elemanın, değeri, aralığı ve sub array'ini return eder
def minSubArr(arr, l, h):

  if (l == h):
    return arr[l], arr[l:h],l, h 

  m = int((l + h)/2)
  temp = []  # return değeri atamak için , gereksiz değişken
  
  leftSum, temp, l1, h1  = minSubArr(arr, l, m)
  rightSum, temp, l2, h2  = minSubArr(arr, m+1, h )
  midSum, l3, h3   = midTotal(arr, l, m, h)

  ans = [leftSum, rightSum, midSum]
  index = (list(ans)).index(min(ans))   # en küçük değerin index'i

  # hangi eleman en küçükse, onun değeri, aralığı ve sub array'i 
  # return edilir 
  if index == 0:
    return leftSum, arr[l1:h1+1], l1, h1
  elif index == 1:
    return rightSum, arr[l2:h2+1], l2, h2
  else:
    return midSum, arr[l3:(h3+1)], l3, h3



def min_subarray_finder(inpArr):
  n = len(inpArr)
  subArr = []
  max_sum, subArr, l, h = minSubArr(inpArr, 0, n-1)
  return subArr
 


inpArr = [1, -4, -7, 5, -13, 9, 23, -1]
msa = min_subarray_finder(inpArr)
print(msa)
#Output: [-4, -7, 5, -13]
print(sum(msa))
#Output: -19