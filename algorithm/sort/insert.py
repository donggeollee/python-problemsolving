import random

def insert_sort(to_sort_list) :
    for i in range(len(to_sort_list)-1) :
        for j in range(i+1,0,-1) :
            if to_sort_list[j] < to_sort_list[j-1] :
                to_sort_list[j] ,to_sort_list[j-1] = to_sort_list[j-1], to_sort_list[j]
            else :
                break
    return to_sort_list

data_list = random.sample(range(100), 20) 
print(data_list)
print(insert_sort(data_list))
