import cv2
import numpy as np
import os

# Resmin klasör yolunu otomatik ayarlar
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "klon.jpg")

img = cv2.imread(image_path, 0)
# Resmi gri tonlamalı (siyah-beyaz) olarak belleğe okur.

# kernel = np.ones((5, 5), np.uint8)
# erosion = cv2.erode(img, kernel, iterations=1)
# cv2.imshow("img", img)
# cv2.imshow("erosion", erosion)
# Aşındırma (Erosion): Ön plandaki beyaz nesneleri aşındırır/inceletir (Siyah alanlar artar, parazitler küçülür).

# kernel = np.ones((5, 5), np.uint8)
# dilation = cv2.dilate(img, kernel, iterations=5)
# cv2.imshow("img", img)
# cv2.imshow("dilaiton", dilation)
# Genişletme (Dilation): Ön plandaki beyaz nesneleri genişletir/kalınlaştırır (Beyaz alanlar artar, nesneler birleşir).

# kernel = np.ones((5, 5), np.uint8)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# cv2.imshow("img", img)
# cv2.imshow("opening", opening)
# Açma (Opening): Önce Aşındırma sonra Genişletme yapar. Nesnelerin dışındaki küçük beyaz gürültüleri/noktaları temizler.

# kernel = np.ones((5, 5), np.uint8)
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# cv2.imshow("img", img)
# cv2.imshow("closing", closing)
# Kapama (Closing): Önce Genişletme sonra Aşındırma yapar. Nesnelerin içindeki küçük siyah delikleri ve boşlukları kapatır.

# kernel = np.ones((5, 5), np.uint8)
# gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# cv2.imshow("img", img)
# cv2.imshow("gradient", gradient)
# Morfolojik Gradyan: Genişletme ile Aşındırma arasındaki farkı alır. Nesnelerin dış sınırlarını/kenar çizgilerini ortaya çıkarır.

kernel = np.ones((5, 5), np.uint8)
# Morfolojik işlem için 5x5 boyutunda 1'lerden oluşan filtre (kernel) matrisi oluşturur.

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# Top Hat (Şapka Dönüşümü): Orijinal resim ile Açma (Opening) uygulanmış resim arasındaki farkı alır. Arka plandan daha parlak nesneleri öne çıkarır.

cv2.imshow("img", img)
# Orijinal gri resmi "img" başlıklı pencerede gösterir.

cv2.imshow("tophat", tophat)
# Top Hat filtresi uygulanmış sonucu "tophat" penceresinde gösterir.

cv2.waitKey(0)
cv2.destroyAllWindows()