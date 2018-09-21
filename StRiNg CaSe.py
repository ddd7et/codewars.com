#https://www.codewars.com/kata/52b757663a95b11b3d00062d/solutions/python

#Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

#The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').
#Examples:

#to_weird_case('String'); # => returns 'StRiNg'
#to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'


def to_weird_case(string):
    new_string = ""
    i = 0

    for s in string:
        if s == " ":
            i = 0
            new_string += " "
            continue
            
        if i % 2 == 0:
            new_string += s.capitalize()
        else:
            new_string += s.lower()
        i += 1
    return new_string

print(to_weird_case("thisis Is A teSt"))
