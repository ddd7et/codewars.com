#https://www.codewars.com/kata/exes-and-ohs/train/python
#Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

#Examples input/output:

#XO("ooxx") => true
#XO("xooxx") => false


def xo(s):
    return len([x.lower() for x in s if x =="o" or x == "O"]) == len([x.lower() for x in s if x =="x" or x=="X"])
