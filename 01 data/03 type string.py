
Str = "Zwykły tekst!"
print(Str)
print(len(Str)) # wypisuje liczbę znaków z zmiennej string zaczynajac od 1
print(type(Str))

print(Str[len(Str)-1]) # odwlołanie do znaku w nawiach [] zaczyna od 0 

print(Str[0:5]) # odwlołanie do znaku, liczy znaki od 0 

StrX3 = (Str +" ") *3 # mnożenie i sumowanie tekstu
print(StrX3)

print(Str[2:]) # pobieranie od 2 do konca znaków

print(Str[::2]) # 1 element +  wybieranie co 2 wyraz

print(Str[0]) # wybór litery z zmiennej tekstu string
print(Str[1])
print(Str[2])
print(Str[3])
print(Str[4])

print(Str[1:4]) # wypisywanie częsci znaków
print(Str[1:5]) # ostatnia liczba wypisywania nie liczona włącznie

print(Str*3) # mnożenie tekstu

Str2 = " World" #sumowanie tekstu
print(Str+Str2)

Str3 = """
Rozbudowany na 
kilka lini tekst """
print(Str3)

Str4= "Pierwsza linia \n druga linia \t tabulacja \n trzecia linia"
print(Str4)

Str5= "cudzysłow \"możliwe\" " # po \ 
print(Str5) 