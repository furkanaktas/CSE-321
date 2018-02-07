#http://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/
#buradan yardım alınmıştır.

"""
array'lerin mid  ler toplamı  k dan küçükse 
    
    1. arrayin mid elemanı, 2. array'in mid elemanından büyükse 
        2. arrayin mid2'ye kadar olan kısmı yoksayılır
    2>1  ise
        1. nin  mid1'e kadar olan ksımı yok sayılır

midler toplamı büyükse
    
    1. arrayin mid elemanı, 2. array'in mid elemanından büyükse 
        1. arrayin mid1'den sonraki kısmı yoksayılır
    2>1  ise
        2. nin  mid2'den sonraki ksımı yok sayılır

"""
def kth_1(arr1, arr2, k):

    if len(arr1) == 0:
        return arr2[k]
    elif len(arr2) == 0:
        return arr1[k]

    mid1 = int(len(arr1)/2)
    mid2 = int(len(arr2)/2)
   
    if mid1+mid2 < k :
        if arr1[mid1] > arr2[mid2]:
            return kth_1(arr1, arr2[mid2+1:], k-mid2-1)
        else:
            return kth_1(arr1[mid1+1:], arr2, k-mid1-1)
    else:
        if arr1[mid1]>arr2[mid2]:
            return kth_1(arr1[:mid1], arr2, k)
        else:
            return kth_1(arr1, arr2[:mid2], k)


def find_kth_book_1(arr1, arr2, k):
    return kth_1(arr1, arr2, k-1)
    

m = ["algortihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming", "oop"]

book = find_kth_book_1(m, n, 4)
print(book)

book = find_kth_book_1(m, n, 6)
print(book)
