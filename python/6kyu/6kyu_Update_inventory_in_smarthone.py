#You will be given an array which lists the current inventory of stock in your store and another array which lists the new inventory being delivered to your store today.

#Your task is to write a function that returns the updated list of your current inventory in alphabetical order.
#Example

#cur_stock = [(25, 'HTC'), (1000, 'Nokia'), (50, 'Samsung'), (33, 'Sony'), (10, 'Apple')]
#new_stock = [(5, 'LG'), (10, 'Sony'), (4, 'Samsung'), (5, 'Apple')]

#update_inventory(cur_stock, new_stock)  ==>
#[(15, 'Apple'), (25, 'HTC'), (5, 'LG'), (1000, 'Nokia'), (54, 'Samsung'), (43, 'Sony')]

def takeSecond(elem):
    return elem[1]
def update_inventory(cur_stock, new_stock):
    answ_stock = []
    found = False
    for c1, s1 in cur_stock:
        #print("c1=%s, s1=%s" %(c1,s1))
        found = False
        
        for c2, s2 in new_stock:
            if s1 == s2:
                answ_stock.append((c1+c2, s1))  
                found = True
                break   
    
        if not found:
            answ_stock.append((c1, s1))

    for c2, s2 in new_stock:
        #print("c1=%s, s1=%s" %(c1,s1))
        found = False
        
        for c1, s1 in cur_stock:
            if s1 == s2:  
                found = True
                break   
    
        if not found:
            answ_stock.append((c2, s2))



    return sorted(answ_stock, key=takeSecond)