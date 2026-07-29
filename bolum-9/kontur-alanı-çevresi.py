import cv2
import os

# Resmin klasör yolunu otomatik ayarlar
script_dir = os.path.dirname(__file__)

# Harita resmini (8.1 map.jpg.jpg) otomatik olarak arar
map_image = "8.1 map.jpg.jpg" if os.path.exists(os.path.join(script_dir, "8.1 map.jpg.jpg")) else "klon.jpg"
image_path = os.path.join(script_dir, map_image)


img = cv2.imread(image_path)

# Resmi varsayılan BGR renk formatında belleğe okur.

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Kontur tespiti yapabilmek için resmi gri tonlamalı (siyah-beyaz) formata dönüştürür.

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# 127 eşik değeriyle ikili (Binary - Siyah/Beyaz) eşikleme uygular.

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Siyah-beyaz resimdeki nesnelerin dış hatlarını (konturlarını) bulup 'contours' listesine kaydeder.

cnt = contours[0]
# Bulunan ilk kontur nesnesini 'cnt' isimli değişkene atar.

area = cv2.contourArea(cnt)
# İlk kontur nesnesinin alanını (içindeki piksel sayısını) hesaplar.

print(area)
# Hesaplanan kontur alan değerini terminale/konsola yazdırır.

M = cv2.moments(cnt)
# İlk kontur nesnesinin görüntü momentlerini (geometrik verilerini) çıkarır.

print(M['m00'])
# Moment verilerindeki 'm00' değerini yazdırır (Bu değer de doğrudan kontur alanına eşittir).

perimeter = cv2.arcLength(cnt, True)
# İlk kontur nesnesinin çevre uzunluğunu hesaplar (True: Şeklin kapalı bir eğri olduğunu belirtir).

print(perimeter)
# Hesaplanan çevre uzunluğunu terminale/konsola yazdırır.

# --- Görseldeki üç tırnak (""") ile yorum satırına alınan gösterim kısmı ---

cv2.imshow("original", img)
# Orijinal renkli resmi "original" penceresinde gösterir.

cv2.imshow("gray", gray)
# Gri tonlamalı resmi "gray" penceresinde gösterir.

cv2.imshow("thresh", thresh)
# Eşikleme yapılmış ikili resmi "thresh" penceresinde gösterir.

cv2.imshow('img', img)
# Orijinal resmi "img" penceresinde gösterir.

cv2.waitKey(0)
cv2.destroyAllWindows()
