import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# Bilgisayarın varsayılan kamerasını (0 numaralı cihaz) başlatır.

def nothing(x):
    pass
# Trackbar kaydırıldığında çalışması zorunlu olan boş geri çağırma (callback) fonksiyonudur.

cv2.namedWindow("Trackbar")
# Kaydırma çubuklarının koyulacağı "Trackbar" isimli pencereyi oluşturur.

cv2.resizeWindow("Trackbar", 500, 500)
# "Trackbar" penceresinin boyutlarını 500x500 piksel yapar.

cv2.createTrackbar("Lower - H", "Trackbar", 0, 180, nothing)
# Alt Renk Tonu (Hue) için 0-180 arası kaydırma çubuğu oluşturur.

cv2.createTrackbar("Lower - S", "Trackbar", 0, 255, nothing)
# Alt Doygunluk (Saturation) için 0-255 arası kaydırma çubuğu oluşturur.

cv2.createTrackbar("Lower - V", "Trackbar", 0, 255, nothing)
# Alt Parlaklık (Value) için 0-255 arası kaydırma çubuğu oluşturur.

cv2.createTrackbar("Upper - H", "Trackbar", 0, 180, nothing)
# Üst Renk Tonu (Hue) için 0-180 arası kaydırma çubuğu oluşturur.

cv2.createTrackbar("Upper - S", "Trackbar", 0, 255, nothing)
# Üst Doygunluk (Saturation) için 0-255 arası kaydırma çubuğu oluşturur.

cv2.createTrackbar("Upper - V", "Trackbar", 0, 255, nothing)
# Üst Parlaklık (Value) için 0-255 arası kaydırma çubuğu oluşturur.

cv2.setTrackbarPos("Upper - H", "Trackbar", 180)
# Üst Hue çubuğunun başlangıç değerini 180 olarak belirler.

cv2.setTrackbarPos("Upper - S", "Trackbar", 255)
# Üst Saturation çubuğunun başlangıç değerini 255 olarak belirler.

cv2.setTrackbarPos("Upper - V", "Trackbar", 255)
# Üst Value çubuğunun başlangıç değerini 255 olarak belirler.

while True:
# Kameradan sürekli anlık görüntü almak için canlı döngü başlatır.

    ret, frame = cap.read()
    # Kameradan anlık kareyi okur.

    if not ret:
    # Kamera kresi alınamazsa döngüyü kırar.
        break

    frame = cv2.flip(frame, 1)
    # Görüntüyü yatay eksende ters çevirerek ayna etkisi verir.

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Görüntüyü BGR renk uzayından HSV renk uzayına dönüştürür.

    lower_h = cv2.getTrackbarPos("Lower - H", "Trackbar")
    # Çubuktaki anlık alt Hue değerini okur.

    lower_s = cv2.getTrackbarPos("Lower - S", "Trackbar")
    # Çubuktaki anlık alt Saturation değerini okur.

    lower_v = cv2.getTrackbarPos("Lower - V", "Trackbar")
    # Çubuktaki anlık alt Value değerini okur.

    upper_h = cv2.getTrackbarPos("Upper - H", "Trackbar")
    # Çubuktaki anlık üst Hue değerini okur.

    upper_s = cv2.getTrackbarPos("Upper - S", "Trackbar")
    # Çubuktaki anlık üst Saturation değerini okur.

    upper_v = cv2.getTrackbarPos("Upper - V", "Trackbar")
    # Çubuktaki anlık üst Value değerini okur.

    lower_color = np.array([lower_h, lower_s, lower_v])
    # Alt sınır değerlerini bir NumPy dizisi haline getirir.

    upper_color = np.array([upper_h, upper_s, upper_v])
    # Üst sınır değerlerini bir NumPy dizisi haline getirir.

    mask = cv2.inRange(frame_hsv, lower_color, upper_color)
    # HSV görüntüsünde belirtilen alt ve üst renk aralığındaki pikselleri beyaz (255), diğerlerini siyah (0) yapan maskeyi oluşturur.

    cv2.imshow("Original", frame)
    # Kameradan gelen orijinal görüntüyü gösterir.

    cv2.imshow("Mask", mask)
    # Oluşturulan renk filtresi (maske) görüntüsünü gösterir.

    if cv2.waitKey(20) & 0xFF == ord("q"):
    # 20 ms bekler; 'q' tuşuna basılırsa döngüyü durdurur.
        break

cap.release()
cv2.destroyAllWindows()
