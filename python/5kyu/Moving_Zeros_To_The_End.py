def move_zeros(array):
    
    new_array = []
    n = 0

    for a in array:
        if type(a) == bool:
            new_array.append(a)
            continue
        if a != 0 and a != 0.0:
            new_array.append(a)
        else:
            n += 1

    for i in range(n):
        new_array.append(0)
    return new_array