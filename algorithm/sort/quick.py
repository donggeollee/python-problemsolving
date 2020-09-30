import random 


data_list = random.sample(range(100),20)

def quick_sort(data):
    if len(data) <= 1:
        return data
    
    left_list, right_list = list(), list()
    pivot = data[0]
    
    for i in range(1, len(data)):
        if pivot > data[i]:
            left_list.append(data[i])
        else:
            right_list.append(data[i])

    return quick_sort(left_list) + [pivot] + quick_sort(right_list)

print(data_list)
print(quick_sort(data_list))


        
