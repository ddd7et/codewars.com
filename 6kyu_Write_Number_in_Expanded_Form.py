#https://www.codewars.com/kata/write-number-in-expanded-form/python
#Write Number in Expanded Form

#You will be given a number and you will need to return it as a string in Expanded Form. For example:

#expanded_form(12) # Should return '10 + 2'
#expanded_form(42) # Should return '40 + 2'
#expanded_form(70304) # Should return '70000 + 300 + 4'

#NOTE: All numbers will be whole numbers greater than 0.


def expanded_form(nums):
    s = nums.__str__()
    str = "0"*len(nums.__str__())
    new_arr = ""
    for i in range (len(str)):
        if s[i] != "0":
            new_arr += s[i]+str[i+1:len(str)] +" + "
             
    return new_arr[0:len(new_arr)-3]