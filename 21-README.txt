Gerekli Çevresel Durumlar

- Python 3.9
- tKinter ( Yüklü değilse `pip install tk`)
- turtle ( Yüklü değilse `pip install turtle`)

Kullanım Adımları
1- Commands.txt dosyasının içine ödev tanımındaki formatta komut satırı girilmeli.
2- Komut satırından (Command Prompt) program başlatılmalı. (`python3 ./main.py`)
3- "Şekli Çiz" Butonuna basılmalı.
4- Commands.txt dosyasına bağlı olarak resim çıkar.

Örnek Komut Satırı
`L 36 [L 4 [F 100 R 60 COLOR K PEN 3] R 10]`

Komut Yönergesi

- "L {sayı}" => Sayı değişkenince döngü döner.
- "F {sayı}" => Sayı değişkenince düz devam eder.
- "R {sayı}" => Sayı değişkenince saat yönünde döner.
- "PEN {sayı}" => Sayı değişkenince kalemin kalınlığı değişir.
- "COLOR {harf}" => Harf değişkenince kalemin rengi değişir.

Renk Paleti

- "K" => Kırmızı
- "M" => Mavi
- "S" => Siyah
- "Y" => Yeşil

Hata Ayıklaması

- COLOR değeri renk paleti dışında renk girişi olursa kullanıcı `alertbox` ile uyarılır ve program kapatılır.
- PEN değeri geçersiz bir değer girilirse kullanıcı `alertbox` ile uyarılır ve program kapatılır.
- R değeri 360 derecenin üstündeyse kullanıcı `alertbox` ile uyarılır ve girilen değer 360'a modlanarak program devam eder.
- F değeri 150'nin üstündeyse kullanıcı `alertbox` ile uyarılır ve girilen değer 150'ye sabitlenerek program devam eder.
- Eğer Commands.txt dosyasında bulunan satır geçerli gramere uygun değilse `errorbox` ile hata mesajı verilir ve program kapatılır.
