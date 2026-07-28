import cv2
import numpy as np
import os

# Resimlerin klasör yolunu otomatik ayarlar
script_dir = os.path.dirname(__file__)

img_filter = cv2.imread(os.path.join(script_dir, "klon.jpg"))
# Ortalama bulanıklaştırma testi için 'klon.jpg' resmini belleğe yükler.

img_median = cv2.imread(os.path.join(script_dir, "klon.jpg"))
# Medyan bulanıklaştırma için 'klon.jpg' resmini belleğe yükler.

img_bilateral = cv2.imread(os.path.join(script_dir, "klon.jpg"))
# Bilateral (İkili) filtreleme için 'klon.jpg' resmini belleğe yükler.


# Resimlerin yüklenip yüklenmediğini kontrol edelim
if img_filter is None or img_median is None or img_bilateral is None:
    print("Hata: '2.png', '3.png' veya '4.png' dosyalarından biri ya da birkaçı bolum-8 klasöründe bulunamadı!")
    print("Lütfen resimleri bolum-8 klasörüne ekleyin veya var olan 'klon.jpg' resmini kullanın.")
else:
    blur = cv2.blur(img_filter, (11, 11))
    # Resme 11x11 boyutunda Ortalama (Mean) Bulanıklaştırma uygular (Piksellerin ortalamasını alarak resmi yumuşatır).

    # blur_g = cv2.GaussianBlur(img_filter, (5, 5), cv2.BORDER_DEFAULT)
    # Gaussian Bulanıklaştırma: Resimdeki gürültüyü azaltmak için piksel ağırlıklarına göre yumuşatma yapar.

    # blur_m = cv2.medianBlur(img_median, 9)
    # Medyan Bulanıklaştırma: Komşu piksellerin ortanca (medyan) değerini alır (Tuz-biber gürültülerini temizlemek için idealdir).

    blur_b = cv2.bilateralFilter(img_bilateral, 9, 75, 75)
    # Bilateral Filtre: Resmin kenar/çizgi keskinliklerini koruyarak yüzeyleri yumuşatır ve pürüzsüzleştirir.

    cv2.imshow("original", img_bilateral)
    # Orijinal resmi "original" başlıklı pencerede gösterir.

    cv2.imshow("blur_b", blur_b)
    # Bilateral filtre uygulanmış yumuşak resmi "blur_b" başlıklı pencerede gösterir.

    cv2.waitKey(0)
    cv2.destroyAllWindows()
