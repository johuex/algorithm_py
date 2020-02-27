def quicksort(arr):
    if len(arr) < 2:
        return arr #базовый случай: маленькие массивы отсортированы
    else: #рекурсивный случай
        pivot  = arr[len(arr)//2]  # опорная точка (в середине списка)
        
        less = [i for i in arr[1:] if i <= pivot] #меньший подмассив

        greater = [i for i in arr[1:] if i > pivot] # больший подмассив

        return quicksort(less) + [pivot] + quicksort(greater) # соединяем отсортированный массив

print (quicksort([10,5,2,3]))


