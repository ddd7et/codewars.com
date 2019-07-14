#https://www.codewars.com/kata/stop-gninnips-my-sdrow/train/csharp

#Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

#Examples:

#spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
#spinWords( "This is a test") => returns "This is a test"
#spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    
    sentence = sentence.split(" ")
    new_sentence = ""

    for x in sentence:
        if len(x)<5:
            new_sentence += x
            new_sentence += " "
        else:
            new_string = ""
            for i in range(len(x)-1, -1, -1):
                new_string += x[i]
            new_string += " " 
            new_sentence += new_string

    return new_sentence[0:len(new_sentence)-1]