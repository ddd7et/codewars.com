

def get_sum(a,b):
    return (x for x in range(min(a,b), max(a,b)+1))

print(type(get_sum(-1,0)))
