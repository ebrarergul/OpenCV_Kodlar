import cv2
import numpy as np
import os

# Resmin klasör yolunu otomatik ayarlar
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "klon.jpg")

img = cv2.imread(image_path, 0)
# Resmi gri tonlamalı (siyah-beyaz) olarak belleğe okur (0 parametresi gri okur).

row, col = img.shape
# Resmin yükseklik (row/satır) ve genişlik (col/sütun) piksel değerlerini alır.

M = cv2.getRotationMatrix2D((col / 2, row / 2), 180, 3)
# 2D Döndürme Matrisini hesaplar: 
# (col/2, row/2): Resmin merkez noktası, 180: Döndürme açısı (derece), 3: Ölçekleme/Büyütme oranı (Resmi 3 kat büyütür).

dst = cv2.warpAffine(img, M, (col, row))
# Hesaplanan döndürme matrisini (M) resme uygular ve döndürülmüş resmi (dst) oluşturur.

cv2.imshow("dst", dst)
# Döndürülmüş ve büyütülmüş resmi "dst" başlıklı pencerede gösterir.

cv2.waitKey(0)
cv2.destroyAllWindows()
