def nth_smallest(arr, pos):
    
    for i in range(pos-1):
    	arr.remove(min(arr))
    
    return min(arr)

arr = [15,20,7,10,4,3]
pos = 3

print(nth_smallest(arr, pos)  )

min[arr.remove(min(arr) for x in range(pos-1))]