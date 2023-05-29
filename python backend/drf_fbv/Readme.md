
## Project create

```powershell
- py -m veneer  ( OR - py manage.py runserver)
- CTRL + C (server durdurur, terminal aktif olur.)
- python manage.py migrate   ( OR - py manage.py migrate)
- py manage.py runserver 
- py manage.py startapp student_api
- pip install python-decouple
- pip freeze > requirements.txt
```
- create .env file and hide SECRET_KEY
- create a gitignore file (https://www.toptal.com/developers/gitignore/api/django)

- go to settings.py -> student_api app ini INSTALLED_APPS ' e ekle;

main/settings.py ->
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # myApps
    'student_api',
]
```

- student_api/models.py dosyasına model ekliyoruz;
student_api/models.py

```py
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
```

- Yeni bir model oluşturduğumuzda yahut modelde bir değişiklik yaptığımızda 'makemigrations' ve 'migrate' çalıştırmamız gerekiyor.

- terminalde;
 
```powershell
- py manage.py makemigrations
- py manage.py migrate
- py manage.py createsuperuser (create -> username, password)
```

- admin panelde modelimize erişebilmek için student_api/admin.py da modelimizi register etmemiz gerekiyor;

student_api/admin.py
```py
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

- terminalden

```powershell
- py manage.py runserver
```

- tarayıcımızdan admin panele geçiş yapıyoruz ->
http://127.0.0.1:8000/admin


```powershell
- pip install djangorestframework
- pip freeze > requirements.txt
```

- go to settings.py -> rest_framework paketini INSTALLED_APPS ' e ekle;

main/settings.py ->

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # myApps
    'student_api',
    # 3rd party packages
    'rest_framework',
]
```

- create a file as serializers.py under the our app.

student_api/serializers.py
```py
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    number = serializers.IntegerField()
```

main/urls.py
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api/', include('student_api.urls')),
]
```

student_api/urls.py
```py
from django.urls import path
from .views import home

urlpatterns = [
    path('', home),
]
```


- serializer için create ve update methodlarını yazıyoruz.

```py
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.number = validated_data.get('number', instance.number)
        instance.save()
        return instance

```


- ModelSerializer dan inherit ederek yaptığımız; 

```py
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['first_name']
        # fields = ['number', 'first_name', 'last_name']
        # exclude = ('id',) 
        fields = '__all__'
```

- exclude ile hariç tutmak istediğimiz fieldları belirtiriz. 

