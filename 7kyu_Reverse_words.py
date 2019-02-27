#https://www.codewars.com/kata/reverse-words/train/python
#Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

#Examples
#"This is an example!" ==> "sihT si na !elpmaxe"
#"double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
  
  text = text.split(" ")
  answ = ""

  for t in text:
      answ += t[::-1]+" "
      
  return answ[:-1]
