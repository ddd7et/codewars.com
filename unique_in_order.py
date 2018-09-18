#https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

#Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

#unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
#unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
#unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(iterable):
    if iterable == []:
        return iterable
    if iterable == '':
        return []
    
    new_iterable = [iterable[0]]
    ind = -1

    for i in range(len(iterable)-1):

	    if i < ind:
		    continue

	    for j in range(i+1, len(iterable)):

		    if iterable[i] != iterable[j]:
			    new_iterable.append(iterable[j])
			    ind = j
			    break
    return new_iterable            

