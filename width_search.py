from collections import deque 
def search(name):
    graph = {} # граф, реализованные на словаре
    search_queue = deque()# очередь тех, кто проверяется
    search_queue += graph[name] # добавляем в очередь
    searched = [] #список проверенных пользователей

    while search_queue: #пока очередь не пуста
        person = search_queue.popleft() #уменьшаем очередь тех, кого надо проверить
        if not person in searched: #если персона не проверена
            if person_is_seller(person): #если персона не продавец
                print (person +" is а mango seller!")
                return True
        else:
            search_queue += graph[person] #заносим друзей персоны в очередь
            searched.append(person) #проверили и добавили в список
    return False

def person_is_seller(name): # проверка на продавца манго
    return name[-1] == 'm' # True или False

search("you")