import cv2

# Kamera indeksini dener (0 veya 1)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("0 numaralı kamera açılamadı, 1 numaralı kamera deneniyor...")
    cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("HATA: Kamera açılamadı! Lütfen Mac Sistem Ayarları -> Gizlilik ve Güvenlik -> Kamera kısmından VS Code / Terminal için kamera izni verildiğinden emin olun.")
else:
    print("Kamera başarıyla açıldı. Görüntü alınıyor...")
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Hata: Kameradan kare okunamadı!")
            break

        frame = cv2.flip(frame, 1)
        edges = cv2.Canny(frame, 100, 200)

        cv2.imshow("frame", frame)
        cv2.imshow("Edges", edges)

        if cv2.waitKey(5) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()

