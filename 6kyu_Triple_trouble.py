#https://www.codewars.com/kata/triple-trouble-1/train/python

#Write a function

#triple_double(num1, num2)

#which takes numbers num1 and num2 and returns 1 if there is a straight triple of a number at any place in num1 and also a straight double of the same number in num2.

#If this isn't the case, return 0
#Examples

#triple_double(451999277, 41177722899) == 1
# num1 has straight triple 999s and num2 has straight double 99s

#triple_double(1222345, 12345) == 0
# num1 has straight triple 2s but num2 has only a single 2

#triple_double(12345, 12345) == 0

#triple_double(666789, 12345667) == 1


def triple_double(num1, num2):
    #code me ^^
    num = "-"
    num += str(num1)
    num += "-"
    #print("num=", num)

    sec = "-"
    sec += str(num2)
    sec += "-"
    #print("sec=", sec)

    for i, s in enumerate(num[1:len(num)-3]):
    
        if num[i] != s and num[i+2] == s and num[i+3] == s and num[i+4] != s:
            #print(s)

            for j, f in enumerate(sec[1:len(sec)-1]):
    
                if sec[j] != f and sec[j+2] == f and sec[j+3] != s and f==s:
                    #print("f=", f)
                    return 1
    return 0