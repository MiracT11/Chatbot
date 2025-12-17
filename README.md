# Excel Tabanlı Fuzzy Matching Chatbot

Bu proje, bir Excel dosyasında yer alan soru–cevap çiftlerini kullanarak çalışan basit bir chatbot uygulamasıdır. 
Kullanıcıdan alınan sorular, veri setindeki mevcut sorular ile metin benzerliği temelinde karşılaştırılarak en uygun cevap üretilmeye çalışılır.

Projede büyük dil modelleri kullanılmamış, bunun yerine metin benzerliği (fuzzy matching) yaklaşımı tercih edilmiştir. 
Bu sayede küçük ve orta ölçekli sık sorulan sorular (FAQ) senaryoları için hafif ve anlaşılır bir çözüm elde edilmiştir.

## Projenin Amacı

Bu çalışmanın amacı, bir chatbot sisteminin temel çalışma mantığını uygulamalı olarak öğrenmek ve metin benzerliği tabanlı yanıt üretme yaklaşımını deneyimlemektir. 
Ayrıca, Excel tabanlı bir yapı kullanılarak sistemin kolayca güncellenebilir olması hedeflenmiştir.

## Çalışma Prensibi

Uygulama, Excel dosyasında bulunan soru ve cevap sütunlarını okuyarak çalışır. 
Kullanıcının girdiği soru, veri setindeki tüm sorularla karşılaştırılır ve benzerlik skorları hesaplanır. 
En yüksek skora sahip soru belirlenir ve bu soruya ait cevap kullanıcıya döndürülür. 
Eğer benzerlik skoru yeterince yüksek değilse, kullanıcıdan soruyu farklı şekilde ifade etmesi istenir.

## Özellikler

- Excel dosyasından dinamik soru–cevap okuma
- Metin benzerliği kullanarak en yakın soruyu tespit etme
- Düşük benzerlik durumlarında hatalı cevap vermeyi önleme
- Kod yapısının sade ve geliştirilebilir olması

## Kullanılan Teknolojiler

- Python  
- pandas  
- Metin benzerliği için fuzzy matching kütüphaneleri (rapidfuzz / fuzzywuzzy)


## Kullanım

Excel dosyasında yer alan soru ve cevap sütunları düzenlendikten sonra uygulama çalıştırılır. 
Kullanıcıdan alınan girdiye göre sistem en uygun cevabı üretir.

## Örnek Kullanım

Kullanıcı: İade süresi kaç gündür?  
Chatbot: Ürün iadesi için yasal süre 14 gündür.

## Geliştirilebilir Yönler

Bu proje temel bir yapı sunmaktadır. İlerleyen aşamalarda metin ön işleme adımları eklenebilir, farklı benzerlik metrikleri denenebilir veya bir web arayüzü ile desteklenebilir.

## Not

Bu proje öğrenme ve deneme amaçlı olarak geliştirilmiştir. 
Daha büyük ve karmaşık chatbot sistemleri için gelişmiş doğal dil işleme yöntemleri tercih edilebilir.


