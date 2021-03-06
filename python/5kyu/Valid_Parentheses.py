#https://www.codewars.com/kata/valid-parentheses/train/python

#Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
#Examples

#"()"              =>  true
#")(()))"          =>  false
#"("               =>  false
#"(())((()())())"  =>  true

#Constraints

#0 <= input.length <= 100

#Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).


def valid_parentheses(string):
    sum = 0
    for c in string:
	    if c !="(" and c!= ")":
		    continue
	    if c == "(":
		    sum += 1
	    else:
		    sum -= 1
	    if sum < 0:
		    return False

    if sum != 0:
	    return False
    else:
	    return True