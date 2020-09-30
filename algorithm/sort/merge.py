import random 

data_list = random.sample(range(100),20)

def merge(left_list, right_list):
    return_list = list()
    left_index = 0
    right_index = 0
    # left, right 둘다 있을 때 
    while len(left_list) > left_index and len(right_list) > right_index:
        if left_list[left_index] < right_list[right_index]:
            return_list.append(left_list[left_index])
            left_index += 1
        else:
            return_list.append(right_list[right_index])
            right_index += 1
    # left만 남았을 때 
    if len(left_list) > left_index and len(right_list) <= right_index:
        # print("left_list : ",left_list)
        # return_list += left_list[left_index+1:] ## 이건 왜 최소값이 나오지??
        return_list += left_list[left_index:]
    # right만 남았을 때 
    if len(left_list) <= left_index and len(right_list) > right_index:
        # print("right_list : ",right_list)
        # return_list += right_list[right_index+1:]
        return_list += right_list[right_index:]

    return return_list

def merge_split(data):
    
    if len(data) <= 1:
        return data

    center = int(len(data)/2)
    left_list = merge_split(data[ : center ])
    right_list = merge_split(data[ center : ])

    return merge(left_list, right_list)

print(data_list)
print(merge_split(data_list))