
listData = [1,2,3,4,5,6]

tupleData = tuple(listData)
print(listData)
print(tupleData)

SetData= set(listData)
print(type(SetData))

frozenSetD=frozenset(SetData)
print(type(frozenSetD))


tupleD1 = (("Ola", 231231), ("Art", 1212))
dictD = dict(tupleD1)
print(type(dictD))
print(dictD)

print(dictD["Ola"])