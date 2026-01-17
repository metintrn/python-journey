import random
from word_list import word_list
# Başlangıç ayarları
secili_kelime=random.choice(word_list)
print("adam asmaca oyununa hoş geldiniz")
print(secili_kelime)
can=6

# Boşluklu kelime oluştur

gizli_kelime=[]

kelime_uzunluğu=len(secili_kelime)
for _ in range(kelime_uzunluğu):
    gizli_kelime.append("_")

print(f"gizli kelime:{gizli_kelime}")

    
# Oyun döngüsü
oyun_bitti=False
tahmin_edilenler=[]

while not oyun_bitti:
    
      #kullnıcıdan harf alıyoruz
    tahmin=input("Bir harf tahmin et").lower()

    #daha önce tahmin etin mi?
    if tahmin in tahmin_edilenler:
        print("bunu daha önce tahmn ettin")
        continue
    else:
        tahmin_edilenler.append(tahmin)



    # HARF EŞİT Mİ?
    for i in range(kelime_uzunluğu):
        if secili_kelime[i]==tahmin:
            gizli_kelime[i]=tahmin

    #CAN (LIVES) SİSTEMİ
    if tahmin not in secili_kelime:
        can-=1
        print(f"yanlış tahnin kalan canlar : {can}")


    if "_" not in gizli_kelime:
        print("oyun bitti")
        oyun_bitti=True
    if can==0:
        print("Kaybettin!")
        oyun_bitti=True


