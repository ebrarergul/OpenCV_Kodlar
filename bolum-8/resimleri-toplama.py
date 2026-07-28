# Resimleri toplayabilmemiz için aynı boyutlarda olması gerekiyor.

import cv2
import numpy as np

circle = np.zeros((512, 512, 3), np.uint8) + 255
# 512x512 piksel boyutunda, 3 renk kanallı (BGR), içi beyaz olan 8-bitlik bir tuval/görsel oluşturur.

cv2.circle(circle, (256, 256), 60, (255, 0, 0), -1)
# Oluşturulan beyaz tuval üzerine merkezi (256, 256), yarıçapı 60 piksel olan içi dolu mavi bir daire çizer.

rectangle = np.zeros((512, 512, 3), np.uint8) + 255
# 512x512 piksel boyutunda, 3 renk kanallı ikinci bir beyaz tuval/görsel oluşturur.

cv2.rectangle(rectangle, (150, 150), (350, 350), (0, 0, 255), -1)
# İkinci tuval üzerine sol üst köşesi (150, 150), sağ alt köşesi (350, 350) olan içi dolu kırmızı bir dikdörtgen çizer.

add = cv2.add(circle, rectangle)
# İki görseli piksel piksel toplar (Toplam piksel değeri 255'i aşarsa 255'te sabitler).

print(add[256, 256])
# Elde edilen birleşik resmin merkez (256, 256) pikselinin BGR renk değerini terminale yazdırır.

cv2.imshow("Circle", circle)
# Çizilen daire görselini "Circle" başlıklı pencerede ekranda gösterir.

cv2.imshow("Rectangle", rectangle)
# Çizilen dikdörtgen görselini "Rectangle" başlıklı pencerede ekranda gösterir.

cv2.imshow("Add", add)
# İki görselin toplanmasıyla oluşan sonucu "Add" başlıklı pencerede ekranda gösterir.

cv2.waitKey(0)
cv2.destroyAllWindows()

