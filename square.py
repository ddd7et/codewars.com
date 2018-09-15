# -*- coding: utf-8 -*-

import math
def is_square(n):
    if n < 0:
        return False    
    if math.sqrt(n) % 1 == 0:
	    return True
    return False

    