
for v in [1,2,3,4]:
    print(v * 2)

for v in ("Ania", "Ola", "Dupa"):
    print(v)

print("------------------------")

for x in "HELLO" :
    print(x)
else:
    print("Koniec pętli")

print("========================")

dictData =  {"Art":123456, "Path": 987456}

for k in dictData: # pętla wypisuje pierw klucze
    print(v)
print("------------------------")
for v in dictData.keys():  # odwołanie do wartości
    print(dictData[v])
print("------------------------")
for k in dictData.keys():   # proste odwołanie do kluczy
    print(v)

for v in dictData.values(): # proste odwołanie do wartości
    print(v)

for k, v in dictData.items(): # odwołanie się jednocześnie do kluczy i wartości
    print(k,v)