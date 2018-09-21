#https://www.codewars.com/kata/554ca54ffa7d91b236000023/solutions/python

#Task

#Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
#Example

#  delete_nth ([1,1,1,1],2) # return [1,1]

#  delete_nth ([20,37,20,21],1) # return [20,37,21]


def delete_nth(order,max_e):
    #order = [1,1,3,3,7,2,2,2,2]
    #max_e = 3
    if order == []:
        return []
    new_order = []
    all = set(order)
    #print(all)
    count_all = [0]*len(all)
    #print(count_all)
    count_all[0] = 1
    mlist = []
    for a in all:
        mlist.append(a)
    dict = {}

    for m in mlist:
        dict[m] = 0

    for o in order:
        dict[o] +=1
        if int(dict[o]) <=max_e:
            new_order.append(o)

    return new_order
