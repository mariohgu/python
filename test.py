
# INSERTION
# def insertion (A):
#     for i in range(1,len(A)):
#         key = A[i]
#         j=i-1
#         while j>=0 and A[j]>key:
#             A[j+1]=A[j]
#             j -= 1
#         A[j+1]=key
#--------------------------------------------------------------------------

#QUICKSORT
# def quicksort(arr,start,end):
#     if start<end:
#         p = partition(arr,start,end)
#         quicksort(arr,start,p-1)
#         quicksort(arr,p+1,end)

# def partition(arr,start,end):
#     store = start
#     pivot = start
#     a[pivot],a[end] = a[end],a[pivot]
#     for i in range(start,end):
#         if a[i]<a[end]:
#             a[i],a[store]=a[store],a[i]
#             store +=1
#         a[store],a[end]=a[end],a[store]
#     return store
#-----------------------------------------------------------
#SELECTION SORT

# def selection(a,start,end):

#     for i in range (start,end):
#         min = i
#         for j in range (i+1,end):
#             if a[min]>a[j]:               
#                 min = j
#         a[min],a[i]=a[i],a[min]

# HEAP SORT

# def heapsort(A):
#     n = len(A)
#     for i in range (n//2,-1,-1):
#         heapi(A,i,n)
#     for i in range (n-1,1,-1):
#         A[0],A[i]=A[i],A[0]
#         heapi(A,0,i)

# def heapi(A,i,n):
#     lft = 2*i+1
#     rgt = 2*i+2
#     if (lft<n and A[lft]>A[i]):
#         largest = lft
#     else:
#         largest = i
#     if rgt<n and A[rgt]>A[largest]:
#         largest=rgt
#     if largest != i:
#         A[i],A[largest]=A[largest],A[i]
#         heapi(A,largest,n)

# #BUCKET SORT
# def bucket_sort(input_list):
#     # Find maximum value in the list and use length of the list to determine which value in the list goes into which bucket 
#     max_value = max(input_list)
#     size = max_value/len(input_list)

#     # Create n empty buckets where n is equal to the length of the input list
#     buckets_list= []
#     for x in range(len(input_list)):
#         buckets_list.append([]) 

#     # Put list elements into different buckets based on the size
#     for i in range(len(input_list)):
#         j = int (input_list[i] / size)
#         if j != len (input_list):
#             buckets_list[j].append(input_list[i])
#         else:
#             buckets_list[len(input_list) - 1].append(input_list[i])

#     # Sort elements within the buckets using Insertion Sort
#     for z in range(len(input_list)):
#         insertion_sort(buckets_list[z])
            
#     # Concatenate buckets with sorted elements into a single list
#     final_output = []
#     for x in range(len (input_list)):
#         final_output = final_output + buckets_list[x]
#     return final_output

# def insertion_sort(bucket):
#     for i in range (1, len (bucket)):
#         var = bucket[i]
#         j = i - 1
#         while (j >= 0 and var < bucket[j]):
#             bucket[j + 1] = bucket[j]
#             j = j - 1
#         bucket[j + 1] = var

from random import randint


def ordenar(A,value,start,final):
    if start>final:
        return 0
    half = (start+final)//2
    if value == A[half]:
        return half
    elif value < A[half]:
        return ordenar(A,value,start,half-1)
    else:
        return ordenar(A,value,half+1,final)
        


if __name__ == '__main__':
    a = sorted([randint(0,150) for a in range(3,79)])
    x = ordenar(a,15,0,len(a))
    print(x)
        


 
   


   
    

    #4,1,5,8,2,6,-7,75,0,-1
    #"a","f","r","e","j"