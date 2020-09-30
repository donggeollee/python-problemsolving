import random

def bubble_sort(to_sort_list):
    for i in range(len(to_sort_list) - 1):
        swap_count = 0
        for j in range(len(to_sort_list) - i - 1):
            if to_sort_list[j] > to_sort_list[j+1] : 
                to_sort_list[j], to_sort_list[j+1] = to_sort_list[j+1], to_sort_list[j]
                swap_count += 1
        if swap_count == 0:
            break
    return to_sort_list

data_list = random.sample(range(100), 50)
print(data_list)
print(bubble_sort(data_list))


