import cv2


cap = cv2.VideoCapture("antalya.mp4")
# Bilgisayardaki antalya.mp4 adlı videoyu okumak için hafızaya alır. (cap, capture yani yakalama kelimesinin kısaltmasıdır).

#Not: Eğitmen altında yorum satırı olarak # cap = cv2.VideoCapture(0) yazmış. Eğer 0 yazılırsa, bilgisayarın içine kayıtlı bir video yerine doğrudan kendi webkamerayı açar

while True:
    #Sonsuz bir döngü başlatır. Videolar binlerce kareden (fotoğraftan) oluştuğu için, bu kareleri bitene kadar art arda, sürekli okuyup ekrana yansıtmak için döngüye ihtiyacımız var.
    ret, frame = cap.read()
    #Döngü her döndüğünde videodan sıradaki 1 kareyi (fotoğrafı) okur.
    #frame: Okunan o anki fotoğrafın/karenin kendisidir.
    #ret (return): Çıktı başarılı mı diye kontrol eden "True/False (Doğru/Yanlış)" değeridir. Eğer kare başarıyla okunduysa True (1), video bittiyse ve okunacak kare kalmadıysa False (0) olur.

    if ret == 0:
        break
        #ve altındaki break Eğer video bittiyse (artık okunacak kare kalmadığı için ret değeri 0'a veya False'a eşitse), break komutuyla o sonsuz döngüyü kırar ve videoyu kapatma aşamasına geçer.

    

    cv2.imshow("Antalya", frame)
    # Az önce 3. satırda okuduğu sıradaki kareyi "Antalya" isimli pencerede gösterir. (Bu işlem döngü içinde çok hızlı yapıldığı için gözümüz bunu video olarak algılar).
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
    #waitKey(10): Her bir kareyi ekranda 10 milisaniye bekletir, sonra diğer kareye geçer. (Bu sayıyı büyütürseniz video ağır çekimde oynar, küçültürseniz çok hızlı oynar).
    #== ord("q"): Video oynarken siz klavyeden İngilizce 'q' (quit) tuşuna basarsanız, yine break komutuyla döngüyü kırar ve videoyu zorla kapatır.

cap.release()
#Döngüden çıkınca videoyu (veya webcami) serbest bırakır. Bu çok önemlidir, eğer yazmazsanız bilgisayarınızın kamerası sürekli açık kalabilir veya video dosyası kilitlenebilir.
cv2.destroyAllWindows()
