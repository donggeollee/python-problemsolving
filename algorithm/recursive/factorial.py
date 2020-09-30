def recursive_func(data):
    print(data)
    if data <= 1 :
        return 1 
    return data * recursive_func(data-1)

print(recursive_func(3))

