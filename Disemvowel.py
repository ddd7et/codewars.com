#https://www.codewars.com/kata/disemvowel-trolls/train/python
#Your task is to write a function that takes a string and return a new string with all vowels removed.

def disemvowel(string): 
    vovwl = [1, 5, 9, 15, 21] 

    new_s = ""
    for s in string:
	    if not any(c in vovwl for c in (ord(s)-64, ord(s)-96 )):
	        new_s += s
    return new_s