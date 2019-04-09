#https://www.codewars.com/kata/maximum-length-difference/train/python
#You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string in the first array and y be any string in the second array.

#Find max(abs(length(x) − length(y)))

#If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

#Example:

#a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
#a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
#mxdiflg(a1, a2) --> 13

#Bash note:

def mxdiflg(a1, a2):
    if a1 == [] or a2 == []:
        return -1
    a1_e = [len(x) for x in a1]
    a2_e = [len(x) for x in a2]
    x1 = abs(max(a1_e) - min(a2_e))
    x2 = abs(min(a1_e) - max(a2_e))
    
    return x1 if x1 >x2 else x2