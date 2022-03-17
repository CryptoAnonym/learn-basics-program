
import math
import random


print(abs(9))
print(abs(-9))  # zwraca wartość bezwględną 


print(math.ceil(11.00001)) # zaokrągla do góry
print(math.floor(11.999999)) # zaokrągla w dół 

print(math.ceil(-11.999999)) # zaokrągla w górę 
print(math.floor(-11.999999)) # zaokrągla w dół 

print("--------------------------------------------------")

data = (22,-23,12,56,35,76,234,564,23,-3,4)

print(max(data))
print(min(data))

print(4**3)
print(pow(4,3)) #Funkcja potegująca (liczba, do ktorej potegi)

print(math.sqrt(256)) # pierwiastek kwadratowy

print(round(12.23123123, 3)) # zaokrągla liczbę do n miejsc po przecinku w tym przypadku n=3
print("--------------------------------------------------")

print(random.random()) # losowa liczba od 0-1

print(random.random()*100) # można przemnożyc

listdata = [1,2,3,4,5,6,7,8,9,10]
print(random.choice(listdata)) # losuje element listy

print(random.randrange(0,100,2)) # liczba losowa od 0-100 co 2 lub podzielna przez 2  

random.shuffle(listdata) # losuje liste 
print(listdata) 