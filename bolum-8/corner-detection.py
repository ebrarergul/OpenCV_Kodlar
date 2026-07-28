import cv2
import numpy as np
import os

# Resmin klasör yolunu otomatik ayarlar
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "klon.jpg")

img = cv2.imread(image_path)
# Resmi varsayılan BGR renk formatında belleğe okur.

img1 = cv2.imread(image_path)
# İkinci resmi (img1) belleğe okur.

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Köşe tespiti yapabilmek için renkli resmi gri tonlamalı (siyah-beyaz) formata dönüştürür.

gray = np.float32(gray)
# Shi-Tomasi köşe tespit algoritması gereği matris elemanlarını float32 veri tipine çevirir.

corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
# Shi-Tomasi yöntemiyle en belirgin köşeleri tespit eder: 
# (50: Bulunacak maksimum köşe sayısı, 0.01: Köşe kalite eşiği, 10: İki köşe arasındaki minimum piksel mesafesi).

corners = np.intp(corners)
# Piksel çizimi yapabilmek için bulunan köşe koordinatlarını tamsayı (integer) formatına dönüştürür.

for corner in corners:
# Tespit edilen her bir köşe koordinatı üzerinde sırayla döngü başlatır.

    x, y = corner.ravel()
    # Köşe matrisini tek boyuta indirgeyerek X ve Y koordinat değerlerini alır.

    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
    # Bulunan köşe noktasına (x, y) kırmızı renkli (0,0,255 BGR), 3 piksel yarıçaplı içi dolu küçük bir daire çizer.

cv2.imshow("corner", img)
# Üzerinde tespit edilen köşeler kırmızı noktalarla işaretlenmiş resmi "corner" penceresinde gösterir.

cv2.waitKey(0)
cv2.destroyAllWindows()
