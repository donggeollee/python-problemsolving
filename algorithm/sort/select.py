import random

def select_sort(to_sort_list):
    for stand in range(len(to_sort_list) - 1):
        lowest = stand
        for index in range(stand+1, len(to_sort_list)) :
            if to_sort_list[lowest] > to_sort_list[index]:
                lowest = index
        to_sort_list[stand], to_sort_list[lowest] =  to_sort_list[lowest], to_sort_list[stand]
    return to_sort_list


data_list = random.sample(range(100), 20)
print(data_list)
print(select_sort(data_list))

