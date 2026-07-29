import cv2
import numpy as np
import os

# Resmin klasör yolunu otomatik ayarlar (Tam olarak '8.1 map.jpg.jpg' görseli hedef alınır)
script_dir = os.path.dirname(__file__)
image_name = "8.1 map.jpg.jpg" if os.path.exists(os.path.join(script_dir, "8.1 map.jpg.jpg")) else "klon.jpg"
image_path = os.path.join(script_dir, image_name)

img = cv2.imread(image_path)
# Belirtilen harita görselini ('8.1 map.jpg.jpg') BGR renk formatında belleğe okur.

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Kontur ve dış örtü tespiti için resmi gri tonlamalı (siyah-beyaz) formata dönüştürür.

blur = cv2.blur(gray, (3, 3))
# Haritadaki parazitleri/pürüzleri azaltmak için 3x3 kutu Ortalama Bulanıklaştırma (Blur) filtresi uygular.

ret, thresh = cv2.threshold(blur, 40, 255, cv2.THRESH_BINARY)
# Eşik değeri 40 olarak belirlenerek pikseller ikili (Binary - 0 ve 255) siyah-beyaz seviyeye getirilir.

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Siyah-beyaz resimdeki harita adalarının/nesnelerinin dış hatlarını (konturlarını) tespit eder.

hull = []
# Hesaplanacak dış bükey örtüleri (Convex Hulls) saklamak için boş bir liste oluşturur.

for i in range(len(contours)):
# Bulunan tüm konturlar üzerinde sırayla döngü başlatır.

    hull.append(cv2.convexHull(contours[i], False))
    # Her bir kontur için dış bükey kapsama örtüsünü (Convex Hull) hesaplar ve 'hull' listesine ekler.

bg = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
# Çizimlerin yapılacağı, orijinal resimle aynı boyutlarda siyah (0) 3 kanallı yeni bir tuval (arka plan) oluşturur.

for i in range(len(contours)):
# Çizimleri arka plan üzerine yapmak için döngü başlatır.

    cv2.drawContours(bg, contours, i, (255, 0, 0), 3, 8)
    # Kontur çizgisini mavi renkli ((255, 0, 0) BGR), 3 piksel kalınlığında tuval üzerine çizer.

    cv2.drawContours(bg, hull, i, (0, 255, 0), 1, 8)
    # Konturu kaplayan dış bükey örtüyü (Convex Hull) yeşil renkli ((0, 255, 0) BGR), 1 piksel kalınlığında çizer.

cv2.imshow("Image", bg)
# Çizgilerin çizildiği siyah tuval görüntüsünü "Image" penceresinde gösterir.

cv2.waitKey(0)
cv2.destroyAllWindows()
