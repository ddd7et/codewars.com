#  https://www.codewars.com/kata/5266876b8f4bf2da9b000362/solutions/python
#  You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

#Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

def likes(names):
    if names == []:
        return "no one likes this"
    
    if len(names) == 1:
        return names[0] + " likes this"
    
    if len(names) == 2:
        return names[0]+" and "+names[1]+" like this"
    
    if len(names) == 3:
        return names[0]+", "+names[1]+" and " + names[2]+" like this"
    
    return names[0]+", "+names[1]+" and "+str(len(names)-2)+" others like this"
    
        