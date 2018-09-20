def to_weird_case(string):
    new_string = ""
    i = 0

    for s in string:
        if s == " ":
            i = 0
            new_string += " "
            continue
            
        if i % 2 == 0:
            new_string += s.capitalize()
        else:
            new_string += s.lower()
        i += 1
    return new_string

print(to_weird_case("thisis Is A teSt"))