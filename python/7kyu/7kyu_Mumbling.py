#https://www.codewars.com/kata/mumbling/train/python
#This time no story, no theory. The examples below show you how to write function accum:

#Examples:

#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"
#The parameter of accum is a string which includes only letters from a..z and A..Z.


def accum(s):
    return "".join([x.capitalize()+x.lower()*(i)+"-" for i,x in enumerate(s)])[:-1]