import math
def get_Divisors(p):
    array = []
    sq = math.sqrt(p)
    for i in range(1,p):
        if p % i == 0:
            array.append(i*i)
    array.append(p*p)

    return array


def list_squared(m, n):
    # your code
    new_array = []
    for i in range(m,n):
        array = get_Divisors(i)
        #print(array)

        square = sum(array)
        #square = 7
        #print(square)
        numb = math.sqrt(square)
        if int(numb) == numb:
            new_array.append([i, square])

    return new_array

print(list_squared(250,500))

P - число

k1*n1 = P
k2*n2 = P
...
km*nm = P


(k1)^2+(k2)^2+...+(km*)^2 = квадрат ли это, то есть u*u или нет

(P/n1)^2+(P/n2)^2+...(P/nm)^2 = квадрат ли это

1/n1^2+1/n2^2+...+1/nm^2 -- квадрат ли это


