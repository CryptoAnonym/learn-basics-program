from functools import reduce

sum = lambda a,b: a + b    # przypisujemy do zmiennej anonimowa funkcje (jednolinijkowa) lambda 
                           #
print(sum(4,5))

def generateLambda(num):
    return lambda a: a * num

doubler = generateLambda(2)     # przypisujemy nasza funkcje do zmiennej oraz podsawiamy argument num 2
tripler = generateLambda(3)     # przypisujemy nasza funkcje do zmiennej oraz podsawiamy argument num 3


print(doubler(4))       # wywołuje naszą funkcje i podstawia pod a 4 
print(tripler(4))       # wywołuje naszą funkcje i podstawia pod a 4 

print(tripler(doubler(4))) # wywołuje naszą pierwszą funkcje potem druga i podstawia pod a 4 

print("-------------------")
                                # funkcje wyrzszego rzędu
listdata = [1,2,3,4,5,6,7]

result = list( map(lambda a: a * 3, listdata))
# map iteruje więc musimy ja zmienić na listę list()
# funkcja map przechodzi po każdym elemencie listy itp i stosuje w niej kolejna funkcje
# map(funkcja,lista) w tym przypadku funkcje lambda 
print(result)

print("-------------------")

result1 = list(filter(lambda a: a>3, listdata ))
# funkcja filtr przechodzi po każdym elemencie 
# i zwraca tylko kiedy zawarta w niej funkcja daje prawdę
# w naszym przypadku sprawdza każdy element listdata czy funkcja lamda jest prawidłowa czli >3

print(result1)

print("-------------------")


result3 = reduce(lambda a,b: a + b, listdata)
# funkcja reduce przechodzi po każdym elemencie np listy i wykonuje kolejncą funkcje
# w tym przypadku lambde ktora sumuje wyrazy, wynik zwraca w jednej całości,

print(result3)