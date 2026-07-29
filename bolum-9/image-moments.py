import cv2
import os

# Resmin klasör yolunu otomatik ayarlar
script_dir = os.path.dirname(__file__)

# Üçgen kontur resmini (5.1 contour.png (1).png) otomatik olarak arar
contour_image = "5.1 contour.png (1).png" if os.path.exists(os.path.join(script_dir, "5.1 contour.png (1).png")) else "klon.jpg"
image_path = os.path.join(script_dir, contour_image)


img = cv2.imread(image_path)

# Resmi varsayılan BGR renk formatında belleğe okur.

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Görüntü momentlerini hesaplayabilmek için resmi gri tonlamalı (siyah-beyaz) formata dönüştürür.

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# Eşikleme uygulayarak nesne hatlarını net ikili (Binary - Siyah/Beyaz) hale getirir.

M = cv2.moments(thresh)
# Siyah-beyaz görüntünün alan ve piksel yoğunluk dağılımını ifade eden Moment değerlerini hesaplar.

X = int(M["m10"] / M["m00"])
# Nesnenin ağırlık/kütle merkezinin X (Yatay) koordinatını hesaplar (m10 / m00 formülü ile).

Y = int(M["m01"] / M["m00"])
# Nesnenin ağırlık/kütle merkezinin Y (Dikey) koordinatını hesaplar (m01 / m00 formülü ile).

cv2.circle(img, (X, Y), 5, (0, 255, 0), -1)
# Hesaplanan ağırlık merkezine (X, Y) yeşil renkli ((0,255,0) BGR), 5 piksel yarıçapında içi dolu bir nokta çizer.

cv2.imshow("img", img)
# Üzerinde ağırlık merkezi yeşil noktayla işaretlenmiş resmi "img" penceresinde gösterir.

cv2.waitKey(0)
cv2.destroyAllWindows()
