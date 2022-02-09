
data = [0,1,2,3,4,5,6,7]

for i in data:
    print(i*2)
print("-------------------")
for i in data:
    if i == 3:
        break    # przełamuje pętle przy wartoći 3 i dalej nie wykonuje
    print(i*2)
print("===================")

for i in data:
    print(i)
print("-------------------")

for i in data:
    if (i == 3 or i == 5):
        continue  # wyklucza tylko wartości wymienione i kontunuje dalej pętle
    print(i)

print("===================")

if 10 >2:
    pass  # pass jest wupełniaczem aby program działał a reszte uzupełnimy później