#https://www.codewars.com/kata/name-to-matrix/python
#Given a name, turn that name into a perfect square matrix (nested array with the amount of arrays equivalent to the length of each array).

#You will need to add periods (.) to the end of the name if necessary, to turn it into a matrix.

#If the name has a length of 0, return "name must be at least one letter"
#Examples

#"Bill" ==> [ ["B", "i"],
#             ["l", "l"] ]

#"Frank" ==> [ ["F", "r", "a"],
#              ["n", "k", "."],
#              [".", ".", "."] ]

import math
def matrixfy(st):

    if st =="":
        return "name must be at least one letter"

    n = len(st)

    if math.sqrt(n)%1 != 0:
      numb = math.sqrt(n) - math.sqrt(n)%1 +1
    else:
      numb = math.sqrt(n)

    matrix = []    
    new_s = ""

    for i in range(int(numb)*int(numb)):
      if i < len(st):
        new_s += st[i]
      else:
        new_s += "."


    temp_matrix = []
    j = 0
    for i in range(1, int(numb)+1):
      for k in range(j, int(numb)+j):
        temp_matrix.append(new_s[k])
      matrix.append(temp_matrix)
      temp_matrix = []
      j = i*int(numb)    
        
    return matrix