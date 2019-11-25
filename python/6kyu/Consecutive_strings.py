#https://www.codewars.com/kata/consecutive-strings/python

#You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
#Example:

#longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

#n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
#Note

#consecutive strings : follow one after another without an interruption


def longest_consec(strarr, k):
    max_string = ""
    if k <1 or k > len(strarr):
        return ""
    for i, a in enumerate(strarr):
	    our_arr = "".join(x for x in strarr[i:i+k])
	    if len(our_arr) > len(max_string):
		    max_string = our_arr
		  
    return max_string