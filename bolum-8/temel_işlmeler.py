import cv2
import numpy as np

img = cv2.imread("C:/Users/Master/Desktop/OpenCV/temel_islemler/klon.jpg")

dimension = img.shape # resmin boyutlarını ve kanal verilerini verir.
print(dimension)

color = img[150, 200] # herhangi bir pixelin renk değerlerini gösterir. Girdiğimiz değerler resmin boyutlarından büyük ise INDEXERROR verir.
print("BGR:", color)

blue = img[150, 200, 0] # 150 200 kaça kaçlık değerlerde aradığımızı temsil ediyor. Mavi değerini öğrenmek istediğimiz için 0 yazdık.
print("blue:", blue)

green = img[150, 200, 1]
print("green:", green)

red = img[150, 200, 2]
print("red:", red)

img[150, 200, 0] = 200 # değerini 200 olarak değiştirdik
print("new blue: ", img[150, 200, 0])

blue1 = img.item(200, 250, 0) # 200 250deki mavi değerini blue1 değerine eşitledik.
print("blue1:", blue1)

img.itemset((200, 250, 0), 175) #itemset NumPy 2.0 ve sonrasınde kaldırıldığı için hata veriyor.
print("new blue1 ", img[200, 250, 0])


cv2.imshow("Klon Asker", img)
cv2.waitKey(0)
cv2.destroyAllWindows()