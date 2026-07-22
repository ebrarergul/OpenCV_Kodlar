import cv2

img = cv2.imread("E:\klon.jpg",0)
#Bilgisayardaki bir resmi okuyup belleğe (img adlı değişkene) alır.
#0 parametresi:** Resmi siyah-beyaz (gri tonlamalı) olarak okumak için kullanılır. (Eğer renkli okumak isterseniz 1 yazılır).
# # print(img)
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
# Resmin gösterileceği pencereyi önceden oluşturur ve ona "image" adını verir.
#cv2.WINDOW_NORMAL: Bu ayar sayesinde açılan resim penceresinin boyutunu farenizle köşelerinden tutup büyütebilir veya küçültebilir.

cv2.imshow("image",img)
#imshow (image show): Okuduğumuz img resmini, az önce adını verdiğimiz "image" penceresinin içinde ekranda gösterir.
cv2.imwrite("E:\klon1.jpg",img)
# (image write): Elimizdeki img resmini (siyah-beyaz halini) bilgisayarımıza yeni bir dosya olarak kaydeder. Yeni dosyanın adını klon1.jpg yapar.
cv2.waitKey(0)
#Pencere açıldıktan sonra programın kapanıp gitmesini engeller. Siz klavyeden herhangi bir tuşa basana kadar pencereyi ekranda sonsuza dek (0 olduğu için) bekletir. Bu satır olmazsa pencere açılıp milisaniyeler içinde geri kapanır, göremezsiniz.
cv2.destroyAllWindows()
# Klavyeden bir tuşa bastığınızda (yani waitKey bittikten sonra), ekranda açık kalan tüm pencereleri hafızadan temizler ve düzgünce kapatır.

