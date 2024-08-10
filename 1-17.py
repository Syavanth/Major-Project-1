my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]


count_dict = {}
for item in my_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print(count_dict)  
