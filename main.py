import random
from word_list import word_list
# Başlangıç ayarları
secili_kelime=random.choice(word_list)
print("adam asmaca oyununa hoş geldiniz")
print(secili_kelime)

# Boşluklu kelime oluştur

gizli_kelime=[]

kelime_uzunluğu=len(secili_kelime)
for _ in range(kelime_uzunluğu):
    gizli_kelime.append("_")
print(f"gizli kelime:{gizli_kelime}")

#kullnıcıdan harf alıyoruz
tahmin=input("Bir harf tahmin et").lower()
# HARF EŞİT Mİ?
for i in range(kelime_uzunluğu):
    if secili_kelime[i]==tahmin:
        gizli_kelime[i]=tahmin
print(f"güncel durum {gizli_kelime}")
    
# Oyun döngüsü
  # Harf kontrolü
  # Yanlış tahmin
  # Kazanma kontrolü

