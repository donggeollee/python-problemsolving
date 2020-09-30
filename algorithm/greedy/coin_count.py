

# 어떠한 물건 값 K원을 동전만으로 지불한다고 할 때 최소 동전 개수 구하기 


# coin_list = [1, 100, 50, 500]

# def find_min_coin_count(coin_list, cost):
#     coin_list.sort(reverse=True)
#     details = []
#     for i in range(len(coin_list)):
#         coin_count = cost // coin_list[i] 
#         cost -= coin_count * coin_list[i] 
#         details.append((coin_list[i],coin_count))
    
#     return cost, details

# print(find_min_coin_count(coin_list,5253))




# 음식 무게 제한이 K인 비행기에 에 최대 칼로리를 가지도록 음식을 넣는 문제
# 음식을 분할해서 넣을 수 있음
# (무게, 가치)

food_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]

def get_max_calorie(food_list, capacity):
    food_list = sorted(food_list, key=lambda x:x[1]/x[0], reverse=True)
    return_capacity = capacity 
    details = list()
    max_value = 0

    for food in food_list:
        if capacity - food[0] >= 0:
            capacity -= food[0]
            max_value += food[1]
            details.append((food[0],food[1],1))
        else :
            farction_ratio = capacity / food[0]
            capacity -= food[0] * farction_ratio
            max_value += food[1] * farction_ratio
            details.append((food[0],food[1],round(farction_ratio,2)))
            break

    return_capacity -= capacity
    return (max_value, return_capacity,  details)

print(get_max_calorie(food_list, 30))


