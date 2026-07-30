import cv2
import numpy as np

img1 = cv2.imread("bolum-10/5.1 coins.jpg.jpg")
# Birinci resmi (bozuk paralar) belleğe okur.

img2 = cv2.imread("bolum-10/5.2 balls.jpg.jpg")
# İkinci resmi (toplar) belleğe okur.

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# Daire tespiti yapabilmek için birinci resmi gri tonlamalı (siyah-beyaz) formata dönüştürür.

gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# Daire tespiti yapabilmek için ikinci resmi gri tonlamalı (siyah-beyaz) formata dönüştürür.

img1_blur = cv2.medianBlur(gray1, 5)
# Birinci gri resimdeki pürüzleri ve gürültüleri yok etmek için 5x5 Medyan Bulanıklaştırma uygular.

img2_blur = cv2.medianBlur(gray2, 5)
# İkinci gri resimdeki pürüzleri ve gürültüleri yok etmek için 5x5 Medyan Bulanıklaştırma uygular.

circles = cv2.HoughCircles(img2_blur, cv2.HOUGH_GRADIENT, 1, img2.shape[0] / 4, param1=200, param2=10, minRadius=15, maxRadius=89)
# Hough Daire Dönüşümü ile ikinci resimdeki daireleri (topları) tespit eder (img2.shape[0]/4: Daire merkezleri arasındaki min. mesafe).

if circles is not None:
# Eğer en az bir daire tespit edildiyse çizim işlemini başlatır.

    circles = np.uint16(np.around(circles))
    # Bulunan dairelerin ondalıklı (float) olan X, Y ve yarıçap (R) değerlerini tamsayıya (uint16) yuvarlar.

    for i in circles[0, :]:
    # Tespit edilen her bir dairenin koordinatları üzerinde sırayla döngü başlatır.

        cv2.circle(img2, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Tespit edilen dairenin etrafına yeşil renkli ((0, 255, 0) BGR), 2 piksel kalınlığında bir çember çizer.

cv2.imshow("img", img2)
# Üzerinde yeşil çemberler çizilmiş olan ikinci resmi "img" penceresinde gösterir.

cv2.waitKey(0)


cv2.destroyAllWindows()

