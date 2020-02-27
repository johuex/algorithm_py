states_needed = set([ "mt", "wa", "or", "id", "nv", "ut", "са", "az"]) #множество штатов
#где нужна передача 

stations = {}# словарь станций и множество штатов, которые ею покрываются
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "са"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()#множество нужных станций

while (states_needed): # пока есть непокрытые штаты
    best_station = None #станция, которая обслуживает больше всего штатов
    states_covered = set() #штаты, которые покрываются этой станцией
    for station, states_for_station in stations.items():#перебираем все станции и находим наилучшую
        covered = states_needed & states_for_station #множ-во станций, не вход в покрытие, которые покрываются текущей станцией
        if len(covered) > len(states_covered): #проверка, покрывает ли станция больше, чем текущая
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
print(final_stations)
