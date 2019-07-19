def digital_root(n):
    
    sum = 0

    if len(str(n)) > 1:
        
        for numb in str(n):
            sum += int(numb)

        return digital_root(sum)
    else:
        return n



n = 45
print(digital_root(0))