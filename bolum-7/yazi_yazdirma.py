import cv2
# OpenCV kütüphanesini projemize dahil ettik.

import numpy as np
# Matris (tuval) oluşturmak için NumPy kütüphanesini 'np' kısaltmasıyla dahil ettik.

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255
# 512x512 piksel boyutunda, 3 renk kanallı (renkli) siyah bir matris oluşturup, her piksele 255 ekleyerek tamamen BEYAZ bir tuval elde ettik.

font1 = cv2.FONT_HERSHEY_SIMPLEX
# Kullanabileceğimiz 1. yazı tipini (fontu) belirledik (Basit/düz font).

font2 = cv2.FONT_HERSHEY_COMPLEX
# Kullanabileceğimiz 2. yazı tipini belirledik (Daha karmaşık/kalın font).

font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
# Kullanabileceğimiz 3. yazı tipini belirledik (El yazısı tarzı font).

cv2.putText(canvas, "OpenCV", (30, 100), font3, 2, (0, 0, 0), cv2.LINE_AA)
# Yazı ekleme fonksiyonunun içindeki parametrelerin sırasıyla anlamları:
# 1. canvas   : Yazının ekleneceği arka planımız (tuval).
# 2. "OpenCV" : Ekrana yazdırılacak metin.
# 3. (30, 100): Yazının başlayacağı (X, Y) koordinatları (Sol kenardan 30 px sağa, Üst kenardan 100 px aşağıya).
# 4. font3    : Yukarıda belirlediğimiz el yazısı fontunu kullandık.
# 5. 2        : Yazının büyüklük çarpanı (Ölçek).
# 6. (0, 0, 0): Yazının rengi BGR formatında (0,0,0 tamamen Siyah demektir).
# 7. LINE_AA  : Yazının kenarlarının tırtıklı değil, daha yumuşak/pürüzsüz görünmesini sağlayan çizgi tipi.

cv2.imshow("Canvas", canvas)
# Üzerine yazı yazdığımız tuvali "Canvas" isimli bir pencerede ekranda gösterdik.

cv2.waitKey(0)
# Klavyeden herhangi bir tuşa basılana kadar pencereyi sonsuza dek açık tuttuk.

cv2.destroyAllWindows()
# Tuşa basıldıktan sonra açık kalan tüm pencereleri düzgünce kapattık.