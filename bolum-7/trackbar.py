import cv2
# OpenCV kütüphanesini projeye dahil eder.

import numpy as np
# Matris ve görüntü işlemleri için NumPy kütüphanesini 'np' takma adıyla dahil eder.

def nothing(x):
    # Trackbar (kaydırma çubuğu) değiştiğinde çağrılacak boş (callback) fonksiyon.
    pass
    # Herhangi bir işlem yapmadan geçer.

img = np.zeros((512, 512, 3), np.uint8)
# 512x512 piksel boyutunda, 3 renk kanallı (BGR), tamamen siyah bir görüntü matrisi oluşturur.

cv2.namedWindow("image")
# "image" adında kontrol penceremizi oluşturur.

cv2.createTrackbar("R", "image", 0, 255, nothing)
# "image" penceresine 0-255 arası değer alan "R" (Kırmızı) kaydırma çubuğunu ekler.

cv2.createTrackbar("G", "image", 0, 255, nothing)
# "image" penceresine 0-255 arası değer alan "G" (Yeşil) kaydırma çubuğunu ekler.

cv2.createTrackbar("B", "image", 0, 255, nothing)
# "image" penceresine 0-255 arası değer alan "B" (Mavi) kaydırma çubuğunu ekler.

switch = "0: OFF, 1: ON"
# Açma/kapama anahtarı trackbar'ı için etiket metnini tanımlar.

cv2.createTrackbar(switch, "image", 0, 1, nothing)
# "image" penceresine 0 (Kapalı) ve 1 (Açık) değerlerini alan switch trackbar'ını ekler.

while True:
    # Program açık kaldığı sürece çalışan sonsuz döngüyü başlatır.
    
    cv2.imshow("image", img)
    # "img" görselini "image" isimli pencerede anlık olarak görüntüler.
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        # Klavyeden 'q' tuşuna basılıp basılmadığını kontrol eder (1 ms bekler).
        break
        # 'q' tuşuna basıldıysa döngüden çıkar.

    r = cv2.getTrackbarPos("R", "image")
    # "R" trackbar'ının anlık değerini okur ve 'r' değişkenine atar.

    g = cv2.getTrackbarPos("G", "image")
    # "G" trackbar'ının anlık değerini okur ve 'g' değişkenine atar.

    b = cv2.getTrackbarPos("B", "image")
    # "B" trackbar'ının anlık değerini okur ve 'b' değişkenine atar.

    s = cv2.getTrackbarPos(switch, "image")
    # Anahtar trackbar'ının anlık değerini (0 veya 1) okur ve 's' değişkenine atar.

    if s == 0:
        # Eğer anahtar 0 (OFF / Kapalı) konumundaysa:
        img[:] = [0, 0, 0]
        # Görüntünün tüm piksellerini sıfırlar (siyah yapar).

    if s == 1:
        # Eğer anahtar 1 (ON / Açık) konumundaysa:
        img[:] = [b, g, r]
        # Görüntüyü seçilen BGR (Mavi, Yeşil, Kırmızı) renk değerlerine boyar.

cv2.destroyAllWindows()
# Program sonlanırken açılan tüm OpenCV pencerelerini kapatır.
