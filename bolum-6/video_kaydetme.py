import cv2
# OpenCV kütüphanesini projemize dahil ettik.

cap = cv2.VideoCapture(0)
# Bilgisayarın varsayılan kamerasını (0. kamera) açarak görüntü alır

fileName = "benim_videom.mp4"
# Kaydedilecek videonun adını ve uzantısını belirler

codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# Videonun hangi formatta/sıkıştırma algoritmasında (Mac için MP4V) kaydedileceğini seçer

frameRate = 30
# Videonun saniyedeki kare hızını (FPS - Frame Per Second) 30 olarak belirler

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
resolution = (width, height)
# Hata almamak için kameradan gelen orijinal görüntünün genişlik ve yükseklik değerlerini otomatik alıp videonun çözünürlüğü yapılır.

videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)
# Belirlediğimiz ayarları (isim, format, fps, boyut) kullanarak videoyu kaydetme (yazma) aracını oluşturur.

while True:
# Videoyu oluşturmak için sürekli dönecek sonsuz bir döngü başlatır

    ret, frame = cap.read()
    # Kameradan sıradaki anlık kareyi (fotoğrafı) okuduk. 'ret' okuma başarısını, 'frame' ise görüntüyü tutar.

    if ret == 0:
    # Eğer kameradan görüntü alınamadıysa (ret False/0 ise) hata vermemesi için döngüyü kırıp işlemi durdurmasını sağlar.
        break

    frame = cv2.flip(frame, 1)
    # Kamera görüntüsünü yatay (1) eksende çevirerek ayna yansıması (aynalama) efekti verir.

    videoFileOutput.write(frame)
    # Okunan ve aynalanan o anki kareyi video dosyamızın içine kaydeder.

    cv2.imshow("Webcam Live", frame)
    # O anki kareyi eşzamanlı olarak ekranda "Webcam Live" isimli bir pencerede gösterir.

    if cv2.waitKey(1) & 0xFF == ord("q"):
    # Her kareyi 1 milisaniye beklettik. Eğer bu sırada klavyeden 'q' tuşuna basılırsa...
        break
        # ...döngüyü kır ve videoyu kapat.

videoFileOutput.release()
# İşlem bitince video kaydetme aracını sonlandırıp video dosyasını paketleyerek kapatır.

cap.release()
# Kameramızı serbest bıraktık ki diğer uygulamalar kullanabilsin.

cv2.destroyAllWindows()
# Açık kalan tüm OpenCV pencerelerini sistem hafızasından siler.
