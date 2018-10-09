def persistence(n, mcount=0):
    
    string = str(n)
    #print("count=", mcount)
    #print("string=", string, " len(string)=", len(string))
    if len(string) == 1:
    	#print("Финиш")
    	#print("mcount=", mcount)
    	return mcount
    else:
    	mcount += 1
    	array = []
    	for s in string:
    		array.append(int(s))

    	#print(array)

    	mult = 1
    	for a in array:
    		mult *= a

    	#print("mult=", mult)

    	return persistence(mult, mcount)

#print(persistence(999)  )