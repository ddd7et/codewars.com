#https://www.codewars.com/kata/scramblies/train/python
#Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

#Notes:

#    Only lower case letters will be used (a-z). No punctuation or digits will be included.
#    Performance needs to be considered

#Input strings s1 and s2 are null terminated.

#Examples

#scramble('rkqodlw', 'world') ==> True
#scramble('cedewaraaossoqqyt', 'codewars') ==> True
#scramble('katas', 'steak') ==> False




def scramble(s1, s2):
    
    s1_dict = {}; s2_dict = {}
    
    for i in range(97,123):
        s1_dict[chr(i)] = 0; s2_dict[chr(i)] = 0
    
    for s in s1:
        s1_dict[s] += 1
    for s in s2:
        s2_dict[s] += 1
    
    for count, char in zip(s2_dict.values(), s2_dict.keys()):
        if s1_dict[char] < count:
            return False
    
    return True