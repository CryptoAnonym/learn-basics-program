
function poka()
{
    var liczba1 = document.getElementById("pole1").value;
    var liczba2 = document.getElementById("pole2").value;
    var ciag = "";

    if (liczba1 > liczba2) document.getElementById("pokaz").innerHTML = "Liczba2 musi być wieksza od liczba1" ;
    else if (liczba1 <= liczba2) {
        for (i=liczba1; i<=liczba2; i++)
        {   
        ciag = ciag + i + " "  
        }

        document.getElementById("pokaz").innerHTML = ciag;
    }
    else document.getElementById("pokaz").innerHTML = "Nieprawidlowa wartosc." ;
}    