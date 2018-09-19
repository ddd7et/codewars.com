# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/solutions/python/me/best_practice

#There is an array with some numbers. All numbers are equal except for one. Try to find it!

#findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
#findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55


def find_uniq(arr):

    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            if i>1:
                return arr[i]
            else:
                return arr[i-1]