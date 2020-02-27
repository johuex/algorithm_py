# по возрастанию

def findSmallest(arr):
    '''ищем наименьший элемент и запоминаем его индекс'''
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest)) #добавляем в новый массив 
        #pop - удаляет и возвращает посл элемент или нужный
        #append - добавляет элемент в конец
    return newArr

print (selectionSort([5,3,6,2,10]))