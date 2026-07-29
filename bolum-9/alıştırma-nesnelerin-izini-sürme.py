import cv2
import numpy as np
import os

script_dir = os.path.dirname(__file__)
video_name = "dog.mp4" if os.path.exists(os.path.join(script_dir, "dog.mp4")) else "1.mp4"
video_path = os.path.join(script_dir, video_name)

cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Video bitti veya okunamadı.")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Okunan video karesini BGR renk formatından HSV (Ton, Doygunluk, Parlaklık) renk uzayına dönüştürür.

    sensitivity = 15
    # Renk hassasiyet tolerans değerini 15 olarak belirler (Beyaz rengin ton aralığını esnetmek için kullanılır).

    lower_white = np.array([0, 0, 255 - sensitivity])
    # HSV formatında filtrelenecek beyaz rengin alt sınır değerlerini (H, S, V) oluşturur.

    upper_white = np.array([255, sensitivity, 255])
    # HSV formatında filtrelenecek beyaz rengin üst sınır değerlerini (H, S, V) oluşturur.

    mask = cv2.inRange(hsv, lower_white, upper_white)
    # HSV görüntüsünde belirlenen alt ve üst beyaz renk aralığındaki pikselleri beyaz (255), diğerlerini siyah (0) yapan maskeyi üretir.

    res = cv2.bitwise_and(frame, frame, mask=mask)
    # Orijinal kare ile maskeyi bitsel VE işlemine sokarak sadece beyaz renkli alanları orijinal rengiyle ekranda süzüp ayırır.

    cv2.imshow("frame", frame)
    # Orijinal video karesini "frame" penceresinde gösterir.

    cv2.imshow("mask", mask)
    # Beyaz rengin filtrelendiği siyah-beyaz maske görüntüsünü "mask" penceresinde gösterir.

    cv2.imshow("result", res)
    # Maskeleme sonucu ayıklanan renkli nihai görüntüyü "result" penceresinde gösterir.

    k = cv2.waitKey(5) & 0xFF
    # Her kare arasında 5 milisaniye bekler ve klavyeden basılan tuşun ASCII kodunu alır.

    if k == 27:
    # Eğer klavyeden 'ESC' tuşuna (ASCII kodu 27) basılırsa...
        break
        # Döngüyü kırarak video oynatmayı durdurur.

cap.release()
# Video kaynaklarını serbest bırakır ve temizler.

cv2.destroyAllWindows()

