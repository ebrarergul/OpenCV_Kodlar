# roi ---> region of interest ---> ilgi alanı
import cv2
import os

# Scriptin bulunduğu klasördeki klon.jpg dosyasının tam yolunu otomatik alır
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "klon.jpg")

img = cv2.imread(image_path)

# Resmin yüklenip yüklenmediğini kontrol edelim (NoneType hatasını önler)
if img is None:
    print(f"Hata: Resim bulunamadı veya okunamadı! Aranan yol: {image_path}")
else:
    # print(img.shape[:2]) # resmin boyutunu verir.

    roi = img[15:110, 100:250] # resmin içinden bir parça almamızı sağlar.

    cv2.imshow("Klon", img)
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
