import time
from time import strftime
import cv2
import cv2 as cv  # OpenCV Paketini ekliyoruz.

kamera = cv.VideoCapture(0)  # Kamerayı açıyoruz.

while True:  # Sonsuz döngü, 
    if cv.waitKey(40) == 27:  # eğer ESC tuşuna basılırsa programımız sonlansın
        break

    isOk1, resim1 = kamera.read()  # Bir görüntü okuyoruz. Bu 1 kare resim okunması anlamına geliyor.
    time.sleep(2)
    isOk2, resim2 = kamera.read() # Bir görüntü okuyoruz. Bu 1 kare resim okunması anlamına geliyor.
    #ret, resim1 = kamera.read()
    time.sleep(2)
    #ret, resim2 = kamera.read()
    roi3 = resim1[100:500, 100:400]
    roi4 = resim2[100:500, 100:400]

    fark = cv2.absdiff(roi3, roi4)
    gri = cv2.cvtColor(fark, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gri, (5, 5), 0)
    _, esik = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    genis = cv2.dilate(esik, None, iterations=3)
    kontur, _ = cv2.findContours(genis, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if kontur:
        for a in kontur:
            (x, y, w, h) = cv2.boundingRect(a)
            if cv2.contourArea(a):
                cv2.rectangle(resim1, (x, y), (w + x, h + y), (0, 0, 255), 2)
    else:
        cv2.putText(roi3, "DURUM: {}".format('Fark YOK'), (10, 10), cv2.FONT_HERSHEY_TRIPLEX,
                    0.5, (0, 0, 255), 1)
        tt = strftime("%a, %d %b %Y %H:%M:%S")      



    cv.putText(resim1, 'Resim 1', (50, 50), 2, 1.0, (0, 255, 0))  # Resimler üzerine yazı ekliyoruz
    cv.putText(resim2, 'Resim 2', (50, 50), 2, 1.0, (0, 0, 255))





    fark = cv.absdiff(resim1, resim2)  # iki görselin farkı alınıyor, |a-b|
    cv.imshow("Hareket Penceresi 1", resim1)  # Kameradan aldığımız görseli görüntülüyoruz
    cv.imshow("Hareket Penceresi 2", resim2)
    cv.imshow("Fark Penceresi 2", fark)  # Fark görseli görüntüleniyor.

kamera.release()  # kamerayı durdur.
cv.destroyAllWindows()  # Pencereleri yok et.