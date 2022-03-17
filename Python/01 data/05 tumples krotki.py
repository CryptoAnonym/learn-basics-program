

data = ("one", "two", "three", "four", "five", "six", "seven")
 # ciąg danych (krotka en. Tuple)
 # NIE MUTOWALNE  - brak możliwości nadpisywania oraz kasacji wybranego elementu (del)

print(data[0])
print(data[1])
print(data[2])
print(data[3]) # wypisywanie danych z ciągu, zaczynajac od indexu 0 

print(data[-1])
print(data[-2])
print(data[-3]) #działają ujemne indexy 

print(data[2:5]) # zakres
print(data[:3]) # do trzeciego elementu
print(data[3:]) # od trzeciego elementu
print(data[::2]) # co drugi element zaczynajac od 1

# ! multiTuple = ((1, 2, 3), 5, 44) # krotka wielowymiarowa 

print( "one" in data) #sprawdzanie danej czy znajduje się w krotce 

v = "one"
if v in data: print("Yes") #sprawdzenie cz jest i wyswietlenie 

cars = (("dodge", "ford"), ("mustang")) # wielo krotka - wielowymiarowa

print(cars[0][0])

if "ford" in cars[0]:
    print("Ford znajduje sie w krotce 1 ")

print(data*3) # można mnożyć krotki i sumować





