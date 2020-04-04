def validate_pin(pin):

    for i, p in enumerate(pin):
        if ord(p)<48 or ord(p)>57:
           return False

    return True if i == 3 or i == 5 else False
