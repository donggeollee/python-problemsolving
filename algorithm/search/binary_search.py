
def binary_search(data_list, search_data):
    print(data_list)
    if len(data_list) == 1 and data_list[0] == search_data :
        return True
    elif len(data_list) == 1 and data_list[0] != search_data :
        return False
    elif len(data_list) == 0:
        return False

    center = int(len(data_list)/2)

    if data_list[center] == search_data:
        return True
    elif data_list[center] < search_data:
        return binary_search(data_list[center+1:], search_data)
    else :
        return binary_search(data_list[:center], search_data)

data_list = [i for i in range(100)]

print(binary_search(data_list, 15))



    






