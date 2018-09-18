#https://www.codewars.com/kata/550498447451fbbd7600041c/train/python
#Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

def comp(array1, array2):

    if array1 == [] and  array2 == []:
        return True
    if array1 == [] or array2 == []:
        return False
    
    a1 = array1.copy()
    for a in array1:
        if a*a in array2:
            array2.remove(a*a)
            a1.remove(a)
        else:
            return False

    if a1 != [] or array2 != []:
        return False
    return True