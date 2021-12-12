# case-apps

Bu uygulama python 3.8+ ve nodejs 16.3+ sürümleri ile çalışabilmektedir.

Projeyi docker ile çalıştırmak için yapılması gerekenler: Projenin olduğu klasöre girip girip "Terminal üzerinde docker-compose up --build" yazmanız yeterli ve build işleminden sonra uyugulama otomatik olarak çalışacaktır. Daha sonra http://localhost:3000/ adresinden web uygulamalarını kullanabilirsiniz.

Fakat docker ile çalışan uygulamada sql bağlantısını gerçekleştiremedim. Bu nedenle RandomMatch sayfası db üzerinden veri çekilemediği için docker ile kullanılamamaktadır. Uygulanın RandomMatch sayfasını kullanmak için klasik yöntemleri kullanmak gerekiyor.

Klasik yöntemleri kullanmak için izlenmesi gereken adımlar.

app klasörünün olduğu konumda "pip install -r requirements.txt" komutu ile gerekli paketleri yüklemelisiniz.
Öncelikle nodejs kurulumundan sonra "npm install --global yarn" komutu ile yarn yükleyin daha sonra frontend klasöründeyken "yarn install" ile gerekli pakeleri kurun.
SQLITE3 kurulumu gerekmektedir.
Projeyi klasöründeyken "python3 app/main.py" frontend klasöründeyken "yarn start" komutlarını çalıştırdıktan sonra http://localhost:3000/ adresinden web uygulamalarını kullanabilirsiniz.

*** YORUM SATIRI YAZARKEN BİR PROBLEM OLUŞTU EN SON YAZMAYI DÜŞÜNMÜŞTÜM YETİŞTİREMEDİM. PROJEYİ DEĞERLENDİRME GÖRÜŞMESİNDE KOD ÜZERİNDEN SATIR SATIR ANLATABİLİRİM. ***

ÇALIŞMA SAATLERİ

Projeyi docker ile birlikte çalistimak 1 saatimi aldi Fakat dockerdaki bahsettiğim sql problemi ile yaklaşık 4 saat uğraştım fakat çözemedim.(Toplam 5 saat)
Örnek verileri db ye yazma 1 saat civarı.
Login kısmı toplam 3-4 saat arası.
Webp converter kısmı toplamda 4 saat
Random Match sayfası toplamdad 10 saat civarı.
Toplam süreye 25-30 saat civarı diyebiliriz.

SON DUZENLEMEMLE BIRLIKTE PROJEYI CLONELAYIP DOCKER KURULUMUNU YAPIP ACTIKDAN SONRA TEK YAPMANIZ GEREKEN SEY

"Terminal üzerinde docker-compose up --build" komunutu yazmak ve proje baska hicbirseye ihtiyac duymadan http://localhost:3000/ portu uzerinden calicasaktir.
