def clean(my_list):
    result = []
    for x in my_list:
        if x > 0:
            result.append(x)
    return result

def add(my_list):
    sum = 0
    for x in my_list:
        sum += x
    return sum

passengers = [1, -1, 1, 2, 2, 1, 4, 3, 7, -1, 0, 9, 11, 1, 3]
clean_list = clean(passengers)
total = add(clean_list)

print(clean_list)
print("Total number of passengers is", total)