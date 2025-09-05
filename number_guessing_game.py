#Random kütüphanesini çağırma
import random

#Can ve score tanımlama
health = 3
score = 0 

#Oyun Hakkında Bilgilendirme
print(f"Sayı Tahmin Oyunu\n*********************\nOyun Hakında:\n1-Her yanlış tahminde canınız 1 azalır.\n2-Her doğru tahminde canınız azalmaz iken skorunuz 10 puan artar.\n3-100 puanlık skor elde edince oyunu kazanırsınız.\n4-Herhangi bir  canınız kalmadığında oyunu kaybedersiniz.\n*********************\nCan Sayısı: {health}\nSkor: {score}\n*********************")

#Oyun Döngüsü
while True:
    #Rastgele sayı seçimi
    number = random.randint(1,10)

    try:
        #Kullanıcıdan tahmin alımı
        guessing = int(input("Lütfen 1-10 arasında sayı tahmin ediniz(Çıkış yapmak için 'Q/q'):  "))       
    except ValueError:
        print("Lütfen tahmin olarak sayı giriniz.")
        continue

    #Oyun Algoritması
    if number == guessing:
        health += 1
        score += 10 
        print(f"Doğru tahmin , mevcutta {health} canınız bulunmakta ve {score} puan skorunuz bulunmakta\n*********************\nCan Sayısı: {health}\nSkor: {score}\n*********************")

        if score == 100:
            print(f"Tebrikler oyunu {score} puan ve {health} can ile kazandınız")
            break

    else:
        health -= 1
        print(f"Yanlış tahmin , doğru tahmin {number} olacaktı ,{health} canınız kaldı!!\n*********************\nCan Sayısı: {health}\nSkor: {score}\n*********************")
        
        if health == 0:
            print("Malesef canınız kalmadı, Oyun bitti :(")
            break
        

