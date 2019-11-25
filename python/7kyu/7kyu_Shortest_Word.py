def find_short(s):
    s = s.split()
    return min([len(x) for x in s])
