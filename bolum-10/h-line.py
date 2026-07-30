import cv2
import numpy as np

img = cv2.imread("bolum-10/3.1 h_line.png.png")
# Belirtilen yoldaki resmi varsayılan BGR renk formatında belleğe okur.

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Çizgi tespiti yapabilmek için renkli resmi gri tonlamalı (siyah-beyaz) formata dönüştürür.

edges = cv2.Canny(gray, 75, 150)
# Canny Algoritması ile resimdeki keskin kenarları/çizgileri tespit eder (75: Alt eşik, 150: Üst eşik).

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=200)
# Olasılıksal Hough Çizgi Dönüşümü (HoughLinesP) ile kenar haritasındaki doğru parçalarını tespit eder.

for line in lines:
# Tespit edilen her bir doğru parçası üzerinde sırayla döngü başlatır.

    x1, y1, x2, y2 = line[0] if len(line) == 1 else line
    # Çizginin başlangıç (x1, y1) ve bitiş (x2, y2) piksel koordinatlarını alır.

    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    # Tespit edilen çizgi üzerine yeşil renkli ((0, 255, 0) BGR), 2 piksel kalınlığında çizgi çizer.

cv2.imshow("img", img)
# Üzerinde yeşil çizgiler çizilmiş orijinal resmi "img" penceresinde gösterir.

cv2.imshow("gray", gray)
# Gri tonlamalı resmi "gray" penceresinde gösterir.

cv2.imshow("edges", edges)
# Canny kenar haritası görüntüsünü "edges" penceresinde gösterir.

cv2.waitKey(0)

cv2.destroyAllWindows()

