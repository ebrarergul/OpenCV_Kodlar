import cv2
import numpy as np

vid = cv2.VideoCapture("bolum-10/4.2 line.mp4.mp4")
# Belirtilen yoldaki video dosyasını okumak üzere video yakalayıcı (VideoCapture) nesnesini başlatır.

while True:
# Videodaki tüm kareleri sırayla işlemek için sonsuz bir döngü başlatır.

    ret, frame = vid.read()
    # Videodan sıradaki kareyi okur; başarılıysa 'ret' True, okunan görüntü 'frame' olur.

    frame = cv2.resize(frame, (640, 480))
    # Okunan video karesini daha hızlı işleyebilmek için 640x480 piksel boyutuna yeniden boyutlandırır.

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # hsv range for ...
    # Video karesini renk filtresi uygulamak üzere BGR formatından HSV renk uzayına dönüştürür.

    lower_yellow = np.array([18, 94, 140], np.uint8)
    # Tespit edilmek istenen sarı rengin HSV formatındaki alt sınır değerlerini (H, S, V) belirler.

    upper_yellow = np.array([48, 255, 255], np.uint8)
    # Tespit edilmek istenen sarı rengin HSV formatındaki üst sınır değerlerini (H, S, V) belirler.

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    # Belirlenen sarı renk aralığına giren pikselleri beyaz (255), diğer yerleri siyah (0) yapan maskeyi oluşturur.

    edges = cv2.Canny(mask, 75, 250)
    # Sarı renk maskesi üzerinde Canny algoritmasıyla kenarları/sınır çizgilerini tespit eder (75: Alt eşik, 250: Üst eşik).

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=50)
    # HoughLinesP algoritmasıyla kenar çizgilerinden düzgün doğru parçalarını (çizgileri) bulur.

    for line in lines:
    # Tespit edilen tüm çizgiler üzerinde sırayla döngü başlatır.

        x1, y1, x2, y2 = line[0] if len(line) == 1 else line
        # Çizginin başlangıç (x1, y1) ve bitiş (x2, y2) koordinatlarını alır.

        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
        # Orijinal video karesi üzerine bulunan çizgiyi yeşil renkte ((0, 255, 0) BGR), 5 piksel kalınlığında çizer.

    cv2.imshow("IMG", frame)
    # Üzerine şerit çizgileri çizilmiş olan orijinal video karesini "IMG" penceresinde gösterir.

    if cv2.waitKey(20) & 0xFF == ord('q'):
    # Her kare arasında 20 milisaniye bekler; klavyeden 'q' tuşuna basılırsa...
        break
        # Video akışını durdurarak döngüden çıkar.

vid.release()
# Video dosyasını kapatır ve sistem kaynaklarını serbest bırakır.

cv2.destroyAllWindows()

