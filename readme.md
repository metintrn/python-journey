# 🎮 Hangman (Adam Asmaca) – Python

Bu proje, Python ile yazılmış **terminal tabanlı** klasik Adam Asmaca (Hangman) oyunudur. Proje, Python temellerini (döngüler, listeler, koşullar, modüller) öğrenmek ve pekiştirmek amacıyla geliştirilmiştir.

---

## 🚀 Özellikler

* Rastgele kelime seçimi
* Harf tahmin sistemi
* Yanlış tahminlerde **can (lives)** azaltma
* Aynı harfi tekrar girme engeli
* Kazanma / kaybetme kontrolü
* ASCII art ile adam asmaca görselleri

---

## 📁 Proje Yapısı

```
hangman/
│
├─ hangman.py        # Ana oyun dosyası
├─ word_list.py      # Kelime listesi
└─ art.py            # Logo ve stages (ASCII çizimler)
```

---



---

## 🕹️ Oynanış

1. Oyun başladığında rastgele bir kelime seçilir.
2. Kelimenin harf sayısı kadar `_` ekranda gösterilir.
3. Kullanıcı her turda **bir harf** tahmin eder.
4. * Harf kelimede varsa doğru yerlere yerleşir.
   * Harf yoksa can azalır.
5. * Tüm harfler bulunursa **kazanırsın 🎉**
   * Can biterse **kaybedersin 💀**

---

## 🧠 Kullanılan Python Konuları

* `while` döngüsü
* `for` döngüsü ve `range`
* `if / else` koşulları
* `list` ve `string` farkı
* `import` ve modül kullanımı
* Kullanıcıdan veri alma (`input`)

---

## 📌 Geliştirme Fikirleri

* Zorluk seviyesi (can sayısı değiştirme)
* Kelime kategorileri
* Skor sistemi
* GUI (Tkinter / Pygame)

---

## 👤 Geliştirici

**Ahmet Metin Turan**
Python öğrenme sürecinde geliştirilen mini projedir.

---

## 📜 Lisans

Bu proje eğitim amaçlıdır. İsteyen herkes kullanabilir, geliştirebilir ve paylaşabilir.

---

⭐ Eğer projeyi beğendiysen yıldızlamayı unutma!
