from selenium import webdriver          # pamietamy o paczce
import time


window = webdriver.Chrome("C:\chromedriver.exe")            # ściągamy pod naszą wersję przeglodarki do której piszemy bota drivera i wskazujemy miejsce
window.get("https://orteil.dashnet.org/cookieclicker/")     # na jaką strone ma uddać się przegladarka

time.sleep(1)                                               # czas na ząładowanie strony zanim zacznie klikać :)

cookie = window.find_element_by_xpath("/html/body/div/div[2]/div[15]/div[8]/div[1]")    # przypisujemy elementy  gdzie ma kliknąć (zbadaj element -> kopiuj-> full xpath)
komunikat = window.find_element_by_xpath("/html/body/div[1]/div/a[1]")                  # zrobilem od razu zamukanie okienka z akceptacja plikow cookie :)
komunikat.click()                                                                       # wywołujemy funkcję kliknięcia

ulepszeniaSklepu = window.find_elements_by_xpath("/html/body/div/div[2]/div[19]/div[3]/div[6]/*")       # wszystkie elementy z sklepu ulepszeń
ulepszeniaSklepu.reverse() # odwracamy naszą tablice od końca (czyli od najdroższych ulepszeń)

klikniecia = 0        # zmienna do optymalizacja pętli ktora sprawdza czy można kupić przemdiot 
                      # aby za bardzo nie spowalniać komputera
rate =[1]

def buy_items():                                # definiujemy funkcję do kupowania przedmiotów
    buy_more = False                            # zmienna kupuj wiecej ustawiamy na fałsz
    for item in ulepszeniaSklepu:                                            # tworzymy pętle która nam kupuje przedmioty z sklepu
        if item.get_attribute("class") == "product unlocked enabled":        # sprawdzamy co od różnia na źrodle strony poprzez zbadaj elementy możliwe do zakupu i niedostępne w tym przypadku jest to class
            item.click()                                                     # kupuje przedmiot
            buy_more= True                                                   # kiedy nam już kupi przedmiot zmieniamy ja prawdę
            break                                                            
    if buy_more is True:
        buy_items()    



for i in rate:              # pętla służąca do wyboru ile razy mamy kliknąć  (sprawdza listę rate i dodaje do niej 1 do spełnienia się warunku if)
    if i <=100000000:
        cookie.click()      # kliknięcie w ciasteczko
        i = i +1            # zwiększenie wartości iteratora
        rate.append(i)      # zwiększenie listy o kolejny element
        klikniecia += 1     # zwiekszamy klikniecia o 1  
        if klikniecia == 500:    # jeżeli kliknięcia maja 100 dopiero pętla sprawdza, aby jeszcze przyśpieszyć możemy ustawić wiecej
            buy_items()
            klikniecia = 0                                                           # wracamy nasz licznik do liczby poczatkowej            
                                                                                
    else:
        break
