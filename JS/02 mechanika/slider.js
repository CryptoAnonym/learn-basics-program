var numer = Math.floor(Math.random()*5 ) +1;
var timer1 = 0;
var timer2 = 0;

function ustaw(self)
{
    clearTimeout(timer1);
    clearTimeout(timer2);

    numer = self - 1;

    ukryj();
    setTimeout("zmienfoto()", 500);
}

function ukryj()
{
    $("#slider").fadeOut(500);
}

function zmienfoto()
{
    numer ++; if (numer>5) numer=1;
    var plik = "<img src=\"slajdy/slajd" + numer +".png\" />";
    document.getElementById("slider").innerHTML = plik;
    $("#slider").fadeIn(500);

    timer1 = setTimeout("zmienfoto()",5000);
    timer2 = setTimeout("ukryj()",4500);
}