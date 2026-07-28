import cv2
import numpy as np
# from matplotlib import pyplot as plt  # Bu kütüphane bu kodda kullanılmadığı için yorum satırına alındı.
import os


# Resmin klasör yolunu otomatik ayarlar
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "klon.jpg")

img = cv2.imread(image_path, 0)
# Resmi gri tonlamalı (siyah-beyaz) olarak belleğe okur (Eşikleme işlemleri tek kanallı gri resimlerde yapılır).

ret, th1 = cv2.threshold(img, 150, 200, cv2.THRESH_BINARY)
# Basit Eşikleme (Simple Thresholding): Tüm resimde sabit bir sınır (150) kullanır. Piksel değeri 150'den büyükse 200, küçükse 0 yaparlar.

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 2)
# Uyarlamalı Eşikleme (Mean): Resmi küçük bölgelere (21x21) böler ve her bölgenin ortalamasına göre bölgesel eşikleme yapar.

th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)
# Uyarlamalı Eşikleme (Gaussian): Resmi 21x21 bölgelere böler ve Gauss ağırlıklı ortalamaya göre ışık/gölge farklıklarına uyumlu eşikleme yapar.

cv2.imshow("img-th1", th1)
# Sabit/Basit eşikleme yapılmış görseli "img-th1" penceresinde gösterir.

cv2.imshow("img-th2", th2)
# Ortalama uyarlamalı eşikleme görselini "img-th2" penceresinde gösterir.

cv2.imshow("img-th3", th3)
# Gauss uyarlamalı eşikleme görselini "img-th3" penceresinde gösterir.

cv2.waitKey(0)
cv2.destroyAllWindows()
