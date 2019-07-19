#https://www.codewars.com/kata/find-the-parity-outlier/python

#You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
#Examples

#[2, 4, 0, 100, 4, 11, 2602, 36]
#Should return: 11 (the only odd number)

#[160, 3, 1719, 19, 11, 13, -21]
#Should return: 160 (the only even number)


def find_outlier(integers):

    i = 0
    j = 0
    for m in integers[0:3]:
        if m % 2 == 0:
            i += 1
        else:
            j += 1

    if i > j:

        for a in integers:

            if a % 2 != 0: 
                return a
    else:
        for a in integers:
            if a % 2 == 0: 
                return a


        if i > 1 and j==1:
            return nechet
        if j >1 and i == 1:
            return chet
