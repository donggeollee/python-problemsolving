def sum_list(to_sum_list):
    print(to_sum_list)
    if len(to_sum_list) <= 1:
        return to_sum_list[0]
    return to_sum_list[0] + sum_list(to_sum_list[1:])

print(sum_list([1,2,3,4,5,6,7]))