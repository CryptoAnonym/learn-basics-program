from selenium import webdriver          # pamietamy o paczce
import time


window = webdriver.Chrome("C:\chromedriver.exe")            # ściągamy pod naszą wersję przeglodarki do której piszemy bota drivera i wskazujemy miejsce
window.get("https://orteil.dashnet.org/cookieclicker/")     # na jaką strone ma uddać się przegladarka

time.sleep(1)                                               # czas na ząładowanie strony zanim zacznie klikać :)

cookie = window.find_element_by_xpath("/html/body/div/div[2]/div[15]/div[8]/div[1]")    # przypisujemy elementy  gdzie ma kliknąć (zbadaj element -> kopiuj-> full xpath)
komunikat = window.find_element_by_xpath("/html/body/div[1]/div/a[1]")
komunikat.click()                                                                       # wywołujemy funkcję kliknięcia

ulepszeniaSklepu = window.find_elements_by_xpath("/html/body/div/div[2]/div[19]/div[3]/div[6]/*")       # wszystkie elementy z sklepu ulepszeń

klikniecia = 0        # zmienna do optymalizacja pętli ktora sprawdza czy można kupić przemdiot 
                      # aby za bardzo nie spowalniać komputera
rate =[1]


for i in rate:              # pętla służąca do wyboru ile razy mamy kliknąć  (sprawdza listę rate i dodaje do niej 1 do spełnienia się warunku if)
    if i <=100000:
        cookie.click()      # kliknięcie w ciasteczko
        i = i +1            # zwiększenie wartości iteratora
        rate.append(i)      # zwiększenie listy o kolejny element
        klikniecia += 1     # zwiekszamy klikniecia o 1  
        if klikniecia == 100:    # jeżeli kliknięcia maja 100 dopiero pętla sprawdza, aby jeszcze przyśpieszyć możemy ustawić wiecej
            for item in ulepszeniaSklepu:                                            # tworzymy pętle która nam kupuje przedmioty z sklepu
                if item.get_attribute("class") == "product unlocked enabled":       # sprawdzamy co od różnia na źrodle strony poprzez zbadaj
                    item.click()                                                    #elementy możliwe do zakupu i niedostępne
                    break                                                            # w tym przypadku jest to class
            klikniecia = 0                                                            # wracamy nasz licznik do liczby poczatkowej            
                                                                                
    else:
        break
