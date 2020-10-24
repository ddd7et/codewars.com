#[2,3,5,15,75] 5 [5,5,5,15,70]
#[2,3,5,15,75],20),[20,20,20,20,20]
#[2,3,5,45,45],5),[5,5,5,42,43]
#[2,3,5,45,45],30),[]
#[24,48,22,19,37],30),[30,30,30,30,30]

def min_func(pop):

    v_min = pop[0]
    index = 0

    for i, m in enumerate(pop):
        if m < v_min:
            v_min = m
            index = i

    return v_min, index

def max_func(pop):

    v_max = pop[0]
    index = 0

    for i, m in enumerate(pop):
        if m > v_max:
            v_max = m
            index = i

    return v_max, index


def socialist_distribution(population, minimum):
    pop = population#[2,3,5,15,75]    
    minimum = minimum#5 

    pop = [x-minimum for x in pop]

    print(pop)
    m = -10
    pred_pop = pop.copy()

    while True:
        #print("pop=",pop)
        
        min, min_index = min_func(pop)
        max, max_index = max_func(pop)
        
        if min >=0:
            break

        pop[min_index] +=1
        pop[max_index] -=1

        if pop == pred_pop:
            #print("Выходим, так как pop=",pop, " pred_pop=",pred_pop)
            break

        pred_pop = pop.copy()

    pop = [x+minimum for x in pop]
    min, min_index = min_func(pop)
    print("POP=", pop)
    if min <minimum:
        return []

    return pop 


print(
socialist_distribution([24,48,22,19,37],30)
)
