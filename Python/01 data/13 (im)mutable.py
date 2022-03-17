# immutable(niemutowalne) - int, float, bool, str, tuple, frozenset,
# typy których nie zmianiamy w pamieci

a= 1
addr1 = id(a)

a += 1 
addr2 = id(a)

print(addr1)
print(addr2)

print(addr1 == addr2)

# mutable : list, set, dict - można zmieniać wartości w pamięci

listData = [0,1,2]
addr3 = id(listData)

listData += [3,4,5]
addr4 = id(listData)

print(addr3)
print(addr4)

print(addr3 == addr4)
