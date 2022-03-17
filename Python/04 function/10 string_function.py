
string = "Hellow World AAAAAA !"

print("ala".capitalize())

print(string.capitalize()) # odwraca wielkosc pierwsze litery a reszte zmniejsza
print("Ola, ma kota. Ola ma psa".count("Ola")) # sprawdza ile razy w danym łancuchu znakow wystepuje inny

print("Hello".center(20,"=")) # wyśrodkowuje do danej illosci znakow (20) i zastepuje okreslonym lancuchem (=)

print(string.startswith("Hello")) # sprawdza czy dany łańcuch zaczyna się od jakiegoś ciagu
print(string.endswith("!")) # sprawdza czy dany łańcuch kończy się na jakiems ciagu znakow


print(string.find("Ola")) # sprawdza czy dany łańcuch znakow znajduje się, jeżeli nie zwraca -1
print(string.find("World")) # także sprawdza i wyświetla od ktorego indeksu zaczyna się dane słowo

print(string.rfind("AAAAAA")) # niby liczy od konca ale w tym przypadku nie widze tego

print("2312323".isalnum()) # sprawdza czy sa tam same liczby całkowite
print("2312323sadsd".isalpha()) # sprawdza czy dany ciag ma tylko wartosci literowe
print("sadsd".isalpha())

print("sadsd".islower()) # sprawdza czy wszystkie litery sa male
print("saAdsdA".islower())
print("ASDFASD".isupper()) # sprawdza czy wszystkie wielkie znaki

print("    ".isspace()) # spraedza czy zawiera tylko biale znaki

listdata= ["aaa", "nnn", "ccc"]

print("-|".join(listdata))  # dodje ciąg znaków do innego ciągu rodzielajac np w liscie :)

# .lower() zminiejsza wszystkie znaki, .upper() zwieksza wszystkie znaki  

print("AbdDSExsx".swapcase()) # zamienia wielkość liter 
print("   \n\n\n Hello world ! \n \n       a".lstrip()) # kasuje białe znaki od lewej strony
print("   \n\n\n  Hello world ! \n \n       ".rstrip()) # kasuje białe znaki od prawej strony





