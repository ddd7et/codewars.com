def transl(string):

    if "+" in string:
        string = string.split("+") 

        return int(string[0])+int(string[1])

    if "-" in string:
        string = string.split("-") 
        #print("a=",a)
        return int(string[0])-int(string[1])

    if "del" in string:
        string = string.split("del") 
        #print("a=",a)
        return int(string[0])//int(string[1]) 

    if "times" in string:
        string = string.split("times") 
        #print("a=",a)
        return int(string[0])*int(string[1])

def zero(key = None): #your code here
    if key == None:
        return 0
    string = "0"+key
    return transl(string) 
def one(key = None): #your code here
    if key == None:
        return 1
    string = "1"+key
    return transl(string) 

def two(key = None): #your code here
    if key == None:
        return 2
    string = "2"+key
    return transl(string) 

def three(key = None): #your code here
    if key == None:
        return 3
    string = "3"+key
    return transl(string) 

def four(key = None): #your code here
    if key == None:
        return 4
    string = "4"+key
    return transl(string) 

def five(key = None): #your code here
    if key == None:
        return 5
    string = "5"+key
    return transl(string) 

def six(key = None): #your code here
    if key == None:
        return 6
    string = "6"+key
    return transl(string) 

def seven(key = None): #your code here
    if key == None:
        return 7
    string = "7"+key
    return transl(string)  
    
def eight(key = None): #your code here
    if key == None:
        return 8
    string = "8"+key
    return transl(string) 

def nine(key = None): #your code here
    if key == None:
        return 9
    string = "9"+key
    return transl(string) 

def plus(key = None): #your code here
    print("key=","+"+str(key))
    return "+"+str(key)

def minus(key = None): #your code here
    print("key=","-"+str(key))
    return "-"+str(key)
def times(key = None): #your code here
    print("key=","times"+str(key))
    return "times"+str(key)
def divided_by(key = None): #your code here
    print("del=","del"+str(key))
    return "del"+str(key)

#print(seven(plus(seven())))
print( seven(times(five()))  )
