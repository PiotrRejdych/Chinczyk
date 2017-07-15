import threading
from time import sleep
import random

semafor = threading.Semaphore(1)


def producent():
    global zasob
    zasob = 0

    print "Producent start"

    for i in range(20):
        semafor.acquire()
        print "Producent zajal zasob i wynosi on: " + str(zasob)
        zasob += random.randint(0, 10)
        print "Producent dodal do zasobu i teraz wynosi on: " + str(zasob) + "\n"
        semafor.release()
        sleep(2)



def konsument():
    zbior = 0
    i=0
    print "Konsument start"
    while i < 10 :
        semafor.acquire()
        if (zasob > 0):
            zbior += zasob
            print "Konsument zjada " + str(zasob) + " i ma razem " + str(zbior)
        semafor.release()
        i += 1
        sleep(4)




watki = []
watek = threading.Thread(target=producent)
watki.append(watek)
watek.start()
watek = threading.Thread(target=konsument)
watki.append(watek)
watek.start()
