
from cgitb import reset
from tkinter import *
import tkinter
import requests

app = tkinter.Tk()                  # tworzymy okno 
app.geometry('480x780')             # wymiary okna
app.title("infoMarket 0.5v")        # tytuł programu

#app.configure(background = "#FFFACD")

globale = requests.get("https://api.coinpaprika.com/v1/global")
crypto = requests.get("https://api.coinpaprika.com/v1/tickers")
odpNBP = requests.get("http://api.nbp.pl/api/exchangerates/tables/a?format=json")


if globale.ok == True:                  
    data5 = globale.json() 
if odpNBP.ok == True:                   # sprawdzamy czy odp z serwera jest poprawana (200)
    data8 = odpNBP.json()[0]
if crypto.ok == True:              
    data = crypto.json()
        
    mCap = (data5["market_cap_usd"] / 1000000000000)
    mCapChange = data5["market_cap_change_24h"]
    mCapAth = (data5["market_cap_ath_value"] / 1000000000000)
    mCapAthDate = data5["market_cap_ath_date"]
    volume24 = (data5["volume_24h_usd"] / 1000000000)
    btcd = data5["bitcoin_dominance_percentage"]
    rATH = mCapAth - mCap
    procentodATH = ((rATH) / (mCapAth) * -100)
    strprocentodATH = str(procentodATH)

    table = data8["table"]
    no = data8["no"]
    effectiveDate = data8["effectiveDate"]
    rates = data8["rates"]
        
    def nbp(fiat):
            for rate in rates:
                waluta = rate["currency"]
                tiker2 = rate["code"]
                price4 = rate["mid"]
                if tiker2 == fiat:
                    fiat = tkinter.Label(app, text="|"+ tiker2 + "|" + waluta.upper() + "= " + str(price4)+ " " + "|PLN|" ); fiat.pack()
                else:
                    continue
    def paprica(crypt):
            i = 0
            while i <= 100:
                if i < 100:
                    z = data[i]
                    name = z["name"]
                    tiker = z["symbol"]
                    i += 1 
                    cos = z["quotes"]
                    cos2 = cos["USD"]
                    price = cos2["price"]

                    if tiker == str(crypt) or name == str(crypt) :
                        crypt = tkinter.Label(app, text= "|"+ tiker + "|" + " "+ name + " = "+ str(price)[0:8] +" " + "|USD|"); crypt.pack()
                else:
                    break   
#############################################################
    def nbpAll(fiat):
            for rate in rates:
                waluta = rate["currency"]
                tiker2 = rate["code"]
                price4 = rate["mid"]
                if tiker2 == fiat:
                    fiat = tkinter.Label(app, text="|"+ tiker2 + "|" + waluta.upper() + "= " + str(price4)+ " " + "|PLN|" ); fiat.pack()
                else:
                    continue
    def papricaAll(crypt):
            i = 0
            while i <= 100:
                if i < 100:
                    z = data[i]
                    name = z["name"]
                    tiker = z["symbol"]
                    rank = z["rank"]
                    supply = z["total_supply"]
                    maxSuplay = z["max_supply"]
                    akk = z["last_updated"]
                    i += 1 
                    cos = z["quotes"]
                    cos2 = cos["USD"]
                    price = cos2["price"]

                    mCapTiker = cos2["market_cap"] / 1000000000
                    ath_price = cos2["ath_price"]
                    ath_date = cos2["ath_date"]
                    percent_from_price_ath= cos2["percent_from_price_ath"]
                    
                    change24 = cos2["market_cap_change_24h"]
                    change1 = cos2["percent_change_1h"]
                    change7 = cos2["percent_change_7d"]
                    change30 = cos2["percent_change_30d"]
                    changeY = cos2["percent_change_1y"]

                    if tiker == str(crypt)  or name == str(crypt) :
                        crypt = tkinter.Label(app, text= "|"+ tiker + "|" + " "+ name + " = "+ str(price)[0:8] +" " + "|USD|"); crypt.pack()
                        Label(app, text= "Aktualizacja: "+ str(akk[0:10]) + " " + str(akk[11:19]) + "\nRanking nr: " + str(rank) +  "\n Zmiana ceny w ostatnim czasie: ").pack()
                        Label(app, text=" * 1h: " + str(change1) + " %" +  "\n * 24h: " + str(change24)+ " %"  + "\n * 7d: " + str(change7) 
                        + " %" + "\n * 30d: " + str(change30)+ " %"+ "\n * 1y: " + str(changeY)+ " %" ).pack()

                        Label(app, text= "Market: " + str(mCapTiker)[0:5] + " MLD USD" + "\nATH: " + str(ath_price)[0:6] + " USD" + "\n ATH data: " + ath_date[0:10] + "\n Od ATH: " + str(percent_from_price_ath) + " %" ).pack()

                        if supply == 0:
                            Label(app, text="Monet w obrocie: BRAK DANYCH").pack()      
                        else: 
                            Label(app, text="Monet w obrocie: " + str(supply)).pack()
                        if maxSuplay == 0:
                            Label(app, text="Maxymalna podaż: NIESKOŃCZONA").pack()     
                        else:
                            Label(app, text="Maxymalna podaż: " + str(maxSuplay)).pack()
                else:
                    break  

#############################################################

    tkinter.Label(app, text="Kapitalizacja rynku: " + str(mCap)[0:5] + " BLN USD").pack() 
    tkinter.Label(app, text=" Zmiana w 24h:  " + str(mCapChange) + " %").pack() 
    tkinter.Label(app, text=" ATH kapitalizacji:  " + str(mCapAth)[0:5]+ " BLN USD data: " + str(mCapAthDate[0:10]) + " " + str(mCapAthDate[11:19])).pack() 
    tkinter.Label(app, text=" Zmiana od ATH mCap:  " + str(rATH)[0:5]+ " USD " + strprocentodATH[0:5] + " %").pack() 
    tkinter.Label(app, text=" Volumen w 24h:  " + str(volume24)[0:5]+ " MLD USD").pack() 
    tkinter.Label(app, text=" Dominacja BTC:  " + str(btcd)+ " %").pack()        
    tkinter.Label(app, text=" \n").pack() 
    tkinter.Label(app, text=" Kursy walut NBP dla: "+ table + " " + "numer: " + no + " " 
        + "data:" + " " + effectiveDate).pack()
    tkinter.Label(app, text=" \n").pack()

    nbp("USD")
    nbp("EUR")

    tkinter.Label(app, text=" \n").pack()

    paprica("BTC")
    paprica("ETH")

    ######################################

    dane = Entry(app)           # entry ładuje dane 
    dane.pack()                 # wyświetlamy okienko do ładowania danych

    
    def wyszukaj():                   # definiujemy funkcje ktora wykona sie po kliknieciu przycisku
        nbpAll(str(dane.get()))             # pamietamy o zmianie typu i funkcji get
        papricaAll(str(dane.get()))

    Button(app, text = "📃Wyszukaj: ", command = wyszukaj).pack()       # tworzymy przycisk i przypisujemy funkcje 


    tkinter.Label(app, text=" \n").pack()  
    Button(app, text = "🤘 EXIT", command = quit).pack()    
    

    
    app.mainloop()      # funkcja (petla) aby okienko nie znikało

            
            
        

        



