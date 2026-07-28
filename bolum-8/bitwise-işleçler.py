import cv2
import numpy as np
import os

script_dir = os.path.dirname(__file__)

img1 = cv2.imread(os.path.join(script_dir, "klon.jpg"))
# Birinci görseli belleğe yükler.

img2 = cv2.imread(os.path.join(script_dir, "klon.jpg"))
# İkinci görseli belleğe yükler.

# bit_and = cv2.bitwise_and(img2, img1) 
# Bitsel VE (AND): İki resimde de aynı anda beyaz (1) olan pikselleri beyaz yapar, diğer tüm durumları siyah (0) yapar.

# bit_or = cv2.bitwise_or(img2, img1)
# Bitsel VEYA (OR): İki resimden en az birinde beyaz (1) olan pikselleri beyaz yapar.

# bit_xor = cv2.bitwise_xor(img2, img1)
# Bitsel ÖZEL VEYA (XOR): Pikseller birbirinden farklıysa (biri siyah diğeri beyazsa) beyaz (1), pikseller aynıysa siyah (0) yapar.

# bit_not = cv2.bitwise_not(img2)
# Bitsel DEĞİL (NOT - img2 için): Resmi tersine çevirir; siyah (0) yerleri beyaz, beyaz (1) yerleri siyah yapar.

bit_not2 = cv2.bitwise_not(img1)
# Bitsel DEĞİL (NOT - img1 için): Resmin tüm piksel değerlerini tersine çevirir (Görselin negatifini oluşturur).

cv2.imshow("img1", img1)
# Orijinal birinci resmi gösterir.

cv2.imshow("img2", img2)
# Orijinal ikinci resmi gösterir.

cv2.imshow("bit_not2", bit_not2)
# NOT işlemiyle renkleri ters çevrilmiş resmi gösterir.

#### Siyah 0, Beyaz 1 (veya 255) anlamına gelir.

cv2.waitKey(0)
cv2.destroyAllWindows()
