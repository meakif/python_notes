### Django proje kurulumu:
```py
- python --version (py --version)
- python -m venv env (py -m venv env (py -m venv "name"
  best practice name olarak "env" verilir.))
- ./env/Scripts/activate (virtual environmet imiz olan env imizi
  active ediyoruz. Arkasından django kurumu yapıyoruz.
  active etmeden django kurulumu yaparsak globalimize kurmuş oluruz.)
- deactivate (Bu komut ile virtual environmet imiz olan env imizi
  deactive edebiliyoruz.)
# activate komutu
# MAC/Linux  => source env/bin/activate
# bash  => source env/Scripts/activate
# windows  => env\Scripts\activate
- ./env/Scripts/activate
- pip list
- pip freeze (python installed package, python paketlerinden
  kurulumu yapılan paketleri gösterir.)
- pip install django (djangoyu virtual environmet ımız a kuruyoruz.
  active olduktan sonra djangoyu kurmak önemli. Kurduk ve upgrade pip uyarısı verdi.
  Tavsiye ettiği komutu yazarak pip i upgrade ediyoruz.  )
- python.exe -m pip install --upgrade pip (veya ->  pip install --upgrade pip)
- django-admin --version
- pip freeze (kurulan paketleri versionları ile birlikte görüyoruz.)
- pip freeze > requirements.txt
- django-admin startproject main  (proje kurulumu; main isminde bir proje.
  Eğer bu şekilde kurulursa iç içe dosya oluşturur. ilk dosyaya src diye isimlendirebiliriz.
  Ya da aşağıdaki gibi yazıp projemizin tek bir klasör içerisinde olsun diyebiliriz.)
- django-admin startproject main . (Nokta . bu durumda çok önemlidir çünkü;
  koda, Djangoyu şu an bulunduğunuz dizine kurmasını söyler.
  (nokta . şu anki dizine bir kısayoldur).)
- python manage.py runserver (py manage.py runserver   projeyi çalıştırır.
  Server ı çalıştırır.)(projeyi ayağa kaldırma (default port 8000))(Gelen uyarıda 18 tane default olarak gelen admin, auth,
  contenttypes gibi hazır paketlerle ilgili tablolar var, bunlar henüz
  db ye aktarılmamıştır. Bunları model kısmında db ye aktaracağız.
  Şimdilik sıkıntı yok. Ancak admin panele erişeceksek o zaman
  migrate ve migrations komutlarıyla db ye aktarmamız gerekir.)
- python manage.py runserver 8080  (port numarasını değiştirme. aynı anda iki proje çalıştırmak istersek ikincisini ayağa kaldırırken port numarası ile ayağa kaldırmak önemli)
- CTRL + C (server durdurur, terminal aktif olur.)
```
###### Repodan çektiğimiz bir projeyi requirements deki indirilen paket/versiyonları ile birlikte install etmek için kullanılacak komu ->
```py
- pip install -r requirements.txt
```
#### permission denied hatası alınırsa:
Powershell de permission denied (erişim engeli) hatası alanlar ->
(powershell i yönetici olarak çalıştırıp)  aşağıdaki komutu
powershell 'e girsinler ->
```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```