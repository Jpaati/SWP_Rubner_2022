
arr = [5,6,2,7,1,8,3,2]

#sort the array

begrenzt = 0

def selectionSort(array):
    for s in range(len(array)):
        min_idx = s
        for i in range(s , len(array)):
            print(s, min_idx)
            if array[i] < array[min_idx]:
                min_idx = i
        (array[s], array[min_idx]) = (array[min_idx], array[s])
 
# Driver code
data = [ 7, 2,0, 1, 6, 1, 8 ]
selectionSort(data)

print(data)
        
  