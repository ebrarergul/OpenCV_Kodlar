import cv2
import numpy as np
import os

# Resmin klasör yolunu otomatik ayarlar
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "klon.jpg")

img = cv2.imread(image_path, 0)
# Resmi gri tonlamalı (siyah-beyaz) olarak belleğe okur (0 parametresi gri okunmasını sağlar).

row, col = img.shape
# Resmin yükseklik (row/satır) ve genişlik (col/sütun) piksel değerlerini alır.

M = np.float32([[1, 0, 10], [0, 1, 70]])
# Öteleme (Dönüşüm) matrisini oluşturur: Resmi X ekseninde 10 piksel SAĞA, Y ekseninde 70 piksel AŞAĞI kaydırır.

dst = cv2.warpAffine(img, M, (col, row))
# Dönüşüm matrisini (M) resme uygular ve kaydırılmış yeni görseli (dst) oluşturur.

cv2.imshow("dst", dst)
# Kaydırılan resmi "dst" başlıklı pencerede gösterir.

cv2.waitKey(0)
cv2.destroyAllWindows()
