# Teknik Analiz ve Sentez (Adım 6)

## 1. Terminal Otomasyonu ve Dil Seçimi
Projede **Python** dili tercih edilmiştir. Python'un `subprocess` modülü kullanılarak Unix terminal komutları (tar, cp, ls) üzerinden otomasyon sağlanacaktır.

## 2. Unix I/O ve Dosya Yönetimi
Yedekleme işlemi sırasında Standart Çıktı (stdout) ve Hata Çıktısı (stderr) log dosyalarına yönlendirilecektir (I/O Redirection). 
- `0`: Standart Giriş
- `1`: Standart Çıktı (Başarılı yedekleme kayıtları)
- `2`: Standart Hata (Yedekleme hataları)

## 3. JSON-First Yaklaşımı
Zamanlanmış görevlerin listesi ve yedekleme konfigürasyonları `config.json` dosyasında tutulacaktır. Bu sayede veriler tip güvenli ve taşınabilir olacaktır.
