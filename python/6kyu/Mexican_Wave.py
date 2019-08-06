#Mexican Wave
#wave("hello") => []string{"Hello", "hEllo", "heLlo", "helLo", "hellO"}


def wave(str):
    new_list = []
    for i, s in enumerate(str):
      if ord(s) == 32:
        continue
      new_list.append(str[0:i]+str[i:i+1].capitalize()+str[i+1:])
    
    return new_list  