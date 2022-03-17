
setData = {9, 0, 4, 8, 12, 16}  # tworzenie zestawu

setData.add(20)  # dodawanie elementu do zestawu

setData.discard(0) # kasacja elementu z zestawu

print(type(setData))
print(setData)

for v in setData: # iteracja zestawu
    print(v)


frozenData = frozenset(setData)
print(type(frozenData))



