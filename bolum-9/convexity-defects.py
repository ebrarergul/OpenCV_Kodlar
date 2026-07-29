import cv2
import numpy as np
import os

# Resmin klasör yolunu otomatik ayarlar
script_dir = os.path.dirname(__file__)

# Yıldız resmini otomatik olarak arar (9.1 star.png.png veya 9.1 star.png)
star_image = "9.1 star.png.png" if os.path.exists(os.path.join(script_dir, "9.1 star.png.png")) else "klon.jpg"
image_path = os.path.join(script_dir, star_image)


img = cv2.imread(image_path)

# Resmi varsayılan BGR renk formatında belleğe okur.

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Kontur ve dış bükey kusur tespiti için resmi gri tonlamalı (siyah-beyaz) formata dönüştürür.

_, thresh = cv2.threshold(gray, 127, 255, 0)
# Resmi ikili (Binary - 0 ve 255) siyah-beyaz formata dönüştürür.

contours, _ = cv2.findContours(thresh, 2, 1)
# Siyah-beyaz resimdeki nesnelerin çevre hatlarını (konturlarını) tespit eder.

cnt = contours[0]
# Bulunan ilk kontur nesnesini 'cnt' değişkenine atar.

hull = cv2.convexHull(cnt, returnPoints=False)
# Dış bükey örtü (Convex Hull) nokta indekslerini hesaplar (ConvexityDefects fonksiyonu için returnPoints=False olmalıdır).

defects = cv2.convexityDefects(cnt, hull)
# Dış örtü ile nesnenin gerçek sınırları arasındaki içe çöküklükleri/girintileri (Convexity Defects) hesaplar.

if defects is not None:
    for i in range(defects.shape[0]):
        # Tespit edilen her bir dış bükey kusur (girinti noktası) için sırayla döngü başlatır.
        defect = defects[i, 0] if defects.ndim == 3 else defects[i]
        s, e, f, d = defect
        # Kusur matrisinden [başlangıç indeksi, bitiş indeksi, en derin girinti noktası indeksi, mesafe] değerlerini ayrıştırır.

        start = tuple(cnt[s][0])
        # Dış örtünün başlangıç noktası koordinatlarını (x, y) demet (tuple) olarak alır.

        end = tuple(cnt[e][0])
        # Dış örtünün bitiş noktası koordinatlarını (x, y) demet (tuple) olarak alır.

        far = tuple(cnt[f][0])
        # Nesnenin içe girintili en derin noktasının (en uzak nokta) (x, y) koordinatlarını alır.

        cv2.line(img, start, end, [0, 255, 0], 2)
        # Başlangıç ve bitiş noktaları arasına yeşil renkli ([0,255,0] BGR), 2 piksel kalınlığında dış kapsama çizgisi çizer.

        cv2.circle(img, far, 5, [0, 255, 0], -1)
        # Şeklin içe çökük en derin noktasına (far) yeşil renkli, 5 piksel yarıçaplı içi dolu bir nokta çizer.


cv2.imshow("img", img)
# Çizgiler ve girinti noktaları işaretlenmiş resmi "img" penceresinde gösterir.

cv2.waitKey(0)
cv2.destroyAllWindows()
