import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

# Resmin klasör yolunu otomatik ayarlar
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "klon.jpg")

img = cv2.imread(image_path)
# Resmi varsayılan BGR renk formatında belleğe okur.

b, g, r = cv2.split(img)
# Renkli resmi Mavi (Blue), Yeşil (Green) ve Kırmızı (Red) olmak üzere 3 ayrı renk kanalına ayırır.

cv2.imshow("img", img)
# Orijinal resmi "img" başlıklı pencerede gösterir.

plt.hist(b.ravel(), 256, [0, 256])
# Mavi (B) kanalındaki tüm pikselleri 1D diziye (ravel) çevirip 0-255 arası renk yoğunluk grafik dağılımını (histogramını) hesaplar.

plt.hist(g.ravel(), 256, [0, 256])
# Yeşil (G) kanalındaki piksellerin renk dağılım histogramını hesaplar.

plt.hist(r.ravel(), 256, [0, 256])
# Kırmızı (R) kanalındaki piksellerin renk dağılım histogramını hesaplar.

plt.show()
# Matplotlib kütüphanesi üzerinden hazırlanan renk kanalları grafik penceresini ekranda gösterir.

cv2.waitKey(0)
cv2.destroyAllWindows()
