import cv2
import os

script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "klon.jpg")

img = cv2.imread(image_path)

if img is None:
    print(f"Hata: Resim bulunamadı! Yol: {image_path}")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        area = cv2.contourArea(contours[0])
        perimeter = cv2.arcLength(contours[0], True)
        print("Kontur Alanı:", area)
        print("Kontur Çevresi:", perimeter)
    else:
        print("Kontur bulunamadı.")

    cv2.imshow("original", img)
    cv2.imshow("gray", gray)
    cv2.imshow("threshold", thresh)

    print("Pencereler açıldı. (Pencereler VS Code'un arkasında kalmış olabilir!)")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

