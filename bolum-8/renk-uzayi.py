import cv2
import os

# Resmin yolunu otomatik olarak bulur ve yükler
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "klon.jpg")
img = cv2.imread(image_path)
# Belirtilen yoldaki resmi varsayılan BGR (Mavi-Yeşil-Kırmızı) renk formatında belleğe yükler.

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# OpenCV'nin varsayılan BGR renk uzayındaki resmi RGB renk uzayına dönüştürür.

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# Resmi renk tonu (Hue), doygunluk (Saturation) ve parlaklık (Value) bileşenlerinden oluşan HSV renk formatına dönüştürür.

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Renkli resmi tek kanallı gri tonlamalı (siyah-beyaz) formata dönüştürür.

cv2.imshow("Klon", img)
# Orijinal BGR resmini "Klon" başlıklı pencerede gösterir.

cv2.imshow("Klon RGB", img_rgb)
# RGB formatına dönüştürülen resmi gösterir (OpenCV pencereleri BGR beklediği için renkler farklı/ters görünebilir).

cv2.imshow("Klon HSV", img_hsv)
# HSV formatındaki resmi "Klon HSV" başlıklı pencerede gösterir.

cv2.imshow("Klon GRAY", img_gray)
# Gri tonlamalı (siyah-beyaz) resmi "Klon GRAY" başlıklı pencerede gösterir.

cv2.waitKey(0)
cv2.destroyAllWindows()
