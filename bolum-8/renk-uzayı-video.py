import cv2
import os

# Video dosyasının yolunu otomatik olarak ayarlar
script_dir = os.path.dirname(__file__)
video_path = os.path.join(script_dir, "1.mp4")

cap = cv2.VideoCapture(video_path)
# Belirtilen yoldaki video dosyasını okumak üzere yakalayıcı (VideoCapture) nesnesini başlatır.

while True:
# Videonun karelerini (frame) sırayla okuyabilmek için sonsuz bir döngü başlatır.

    ret, frame = cap.read()
    # Videodan bir sonraki kareyi okur; okuma başarılıysa 'ret' True döner, 'frame' ise görüntüyü tutar.

    if not ret:
    # Eğer video sonlandıysa veya dosya okunamadıysa (ret == False)...
        break
        # Döngüyü sonlandırır.

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Okunan renkli video karesini gri tonlamalı (siyah-beyaz) renk formatına dönüştürür.

    cv2.imshow("Video", frame)
    # İşlenen gri kareyi "Video" başlıklı pencerede ekranda gösterir.

    if cv2.waitKey(30) & 0xFF == ord("q"):
    # Her kare arasında 30 milisaniye bekler; kullanıcı klavyeden 'q' tuşuna basarsa...
        break
        # Döngüyü kırarak videoyu durdurur.

cap.release()
# Açılan video dosyasını ve kamera/video kaynaklarını serbest bırakır.

cv2.destroyAllWindows()
