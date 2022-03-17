# tworzymy słownik czyli klucz + wartość w nawiasach klamrowych oddzielone : i na koncu ,

contacts = {
 "Pati" : 530600569,
 "Mama" : 512588032,
 "Arthur" : 500010047,
}

print(contacts["Mama"])

contacts["Rafał"] = 542145898  # dodanie kolejnego elementu slownika

print(contacts["Rafał"])

print(type(contacts))  # typ klasy
print(len(contacts))   # liczba elementów

print (contacts.keys()) # wyświetla klucze
print (contacts.values())

print(" ") # eneter - odstep

for klucz in contacts:
    print(klucz + " "+ str(contacts[klucz]))  # konwersja wszystkiego do tekstu i wyświetlenie dzieki pentli 

print(" ")

for klucz, wartosc in contacts.items(): # pobranie wszystkich przedmiotów i przypisanie do zmiennych oraz wyswietlenie
    print(klucz, " ", wartosc)