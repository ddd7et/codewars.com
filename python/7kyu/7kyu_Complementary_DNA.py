#https://www.codewars.com/kata/complementary-dna/train/python
#If you want to know more http://en.wikipedia.org/wiki/DNA
#In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side.
#DNA strand is never empty or there is no DNA at all (again, except for Haskell).


def DNA_strand(dna):

    dna_new = ""
    for d in dna:
        if d == "A":
            dna_new += "T"
        elif d == "T":
            dna_new += "A"
        elif d == "G":
            dna_new += "C"
        elif d == "C":
            dna_new += "G"
    return dna_new
