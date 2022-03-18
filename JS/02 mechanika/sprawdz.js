
function spr()
{
    var liczba = document.getElementById("pole").value;

    if (liczba > 0)
    document.getElementById("sprawdz").innerHTML =("Liczba jest: dodatnia. ");
    else if (liczba < 0) 
    document.getElementById("sprawdz").innerHTML =("Liczba jest: ujemna. ");
    else if (liczba == "")  
    document.getElementById("sprawdz").innerHTML =("Brak wartości. ");
    else if (liczba == 0)
    document.getElementById("sprawdz").innerHTML =("Liczba jest: zerem. ");
    else 
    document.getElementById("sprawdz").innerHTML =("Nieprawidłowa wartość.");
} 