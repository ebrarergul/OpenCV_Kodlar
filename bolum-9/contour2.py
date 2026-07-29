import cv2
import os

# Resmin klasör yolunu otomatik ayarlar
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "klon.jpg")

img = cv2.imread(image_path)

if img is None:
    print("Hata: 'klon.jpg' resmi bolum-9 klasöründe bulunamadı! Lütfen resmi bu klasöre ekleyin.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Kontur tespiti için resmi gri tonlamalı (siyah-beyaz) formata dönüştürür.

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# Konturların net ayrışması için 127 eşik değeriyle ikili eşikleme (siyah-beyaz) uygular.

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Siyah-beyaz resimdeki nesnelerin dış hatlarını (konturlarını) bulup 'contours' listesine kaydeder.

cv2.drawContours(img, contours, 0, (0, 0, 255), 3)
# Bulunan 1. konturu (0. indeks) orijinal resmin üzerine kırmızı renkte ((0,0,255) BGR), 3 piksel kalınlığında çizer.
# (Eğer 0 yerine -1 yazarsanız tespit edilen TÜM konturları çizer).

cv2.imshow("contour", img)
# Çizilmiş resimle birlikte "contour" başlıklı pencerede gösterir.

cv2.waitKey(0)
cv2.destroyAllWindows()
