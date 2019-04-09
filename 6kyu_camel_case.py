#Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.
#Examples

#to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

#to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"


def to_camel_case(text):
    if text =="":
        return ""
    string = text
    new_string = []
    temp_string =""
    for s in string:
      if s =="_" or s == "-":
        if temp_string != "":
          new_string.append(temp_string)
        temp_string = ""
      else:
        temp_string += s

    if temp_string != "":
      new_string.append(temp_string)
    string = new_string 
    return "".join(string[0]) +"".join([x.capitalize() for x in string[1:] if x != "_" and x !="-"])  