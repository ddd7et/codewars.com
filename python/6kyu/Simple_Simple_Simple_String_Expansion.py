#https://www.codewars.com/kata/simple-simple-simple-string-expansion/train/python

#Given a string that includes alphanumeric characters ('3a4B2d') return the expansion of that string: The numeric values represent the occurrence of each letter preceding that numeric value. There should be no numeric characters in the final string. Empty strings should return an empty string.

#The first occurrence of a numeric value should be the number of times each character behind it is repeated, until the next numeric value appears.

#string_expansion('3D2a5d2f') == 'DDDaadddddff'

#string_expansion('3abc') == 'aaabbbccc'       # correct
#string_expansion('3abc') != 'aaabc'           # wrong
#string_expansion('3abc') != 'abcabcabc'       # wrong

#If there are two consecutive numeric characters the first one is ignored.

#string_expansion('3d332f2a') == 'dddffaa'

#If there are two consecutive alphabetic characters then the first character has no effect on the one after it.

#string_expansion('abcde') == 'abcde'

#Your code should be able to work for both lower and capital case letters.

#string_expansion('') == ''

def string_expansion(s):
    string = s

    new_string = ""
    for i, s in enumerate(string):
        if s.isdigit():
            if i < len(string)-1:
                if string[i+1].isdigit():
                    continue
                else:
                    new_string += s
        else:
            new_string += s

    string = new_string
    print(new_string)

    found = False
    new_string = ""
    for i, s in enumerate(string):
        if s.isdigit():
            remember_digit = int(s)
            found = True
            continue

        if found:
            new_string += remember_digit*s
        else:
            new_string += s
    return new_string
