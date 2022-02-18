import pyautogui as gui,time
i=0
while True: 
    i+=1                     # pętla pokazująca do 2s pozycje myszki
    pozycja = gui.position()
    print(pozycja)
    time.sleep(4)
    if i == 6: break
