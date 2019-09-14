#https://www.codewars.com/kata/simple-pig-latin/train/python

#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
#Examples

#pig_it('Pig latin is cool') # igPay atinlay siay oolcay
#pig_it('Hello world !')     # elloHay orldway !

def get_index(word):
    for w in word:
        if not ((ord(w) >= 65 and ord(w) <=90) or (ord(w)>=97 and ord(w)<=122)):
            return False
    return True

def pig_it(text):
    text = text.split(" ")
    new_text = []
    for t in text:
        if get_index(t):
            new_text.append( t[1:]+t[0]+"ay")
        else:
            new_text.append(t)

    
    return " ".join(x for x in new_text)