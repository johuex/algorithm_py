#list - список, item - элемент который надо найти
def binary_search(list,item): 
    low = 0 #начало списка
    high = len(list) - 1 #конец списка

    while low <= high: 
        mid = (low + high) // 2 #средний элемент (округ в меньш сторону)
        guess = list[mid]
        if guess == item:
            return mid # вывод найденного значения 
        if guess > item: # сравнение больше меньше 
            high = mid - 1 # число меньше, чем в середине
        else:
            low = mid + 1 # число больше, чем в середине
    return None #значение не найдено 

my_list = [1,3,5,7,9]

print (binary_search(my_list,3))
print (binary_search(my_list,-1))