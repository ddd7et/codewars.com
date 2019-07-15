#https://www.codewars.com/kata/your-order-please/train/python
#Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

#Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

#If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
#Examples

#"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
#"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
#""  -->  ""



def order(sentence):
  sentence = sentence.split(" ")

  dict = {}
  for sent in sentence:
      for s in sent:
          if ord(s) >= 49 and ord(s) <= 57:
              dict[sent] = int(s)
              #dict.append((int(s), sent))

  sorted_list = sorted(dict.values())

  new_str = ""
  for s in sorted_list:

      for k,v in zip(dict.keys(), dict.values()   ):
          if v == s:
              new_str += k+" "
  return new_str[:-1]
