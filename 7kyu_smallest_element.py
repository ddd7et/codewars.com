#https://www.codewars.com/kata/5a512f6a80eba857280000fc/solutions/python
#Input >> Output Examples

#1- nthSmallest({3,1,2} ,2) ==> return (2)

#Explanation:

#Since the passed number is 2 , Then the second smallest element in this array/list is 2

#2- nthSmallest({15,20,7,10,4,3} ,3) ==> return (7)

#Explanation:

#Since the passed number is 3 , Then the third smallest element in this array/list is 7

#3- nthSmallest({2,169,13,-5,0,-1} ,4) ==> return (2)

#Explanation:

#Since the passed number is 4 , Then the fourth smallest element in this array/list is 2 

def nth_smallest(arr, pos):
    
    for i in range(pos-1):
    	arr.remove(min(arr))
    
    return min(arr)