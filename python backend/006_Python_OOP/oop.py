import os
os.system('cls' if os.name=="nt" else 'clear')
# ---------------------------------------------
# ---------------------------------------------
# Python - OOP
# ---------------------------------------------
# OOP = Object Oriented Programming
# Classes -> BluePrint: Mimarların kullandığı mavi şablon kağıdıdır. Obje orada tanımlanmıştır.
# DRY: Don't Repeat Yourself
# ---------------------------------------------
# def print_type(data_list):
#     for data in data_list:
#         print(data, type(data))

# print_type([ 'Akif', 123, 123.45, True, (1,2,3), [1,2,3], lambda x:x ])
# ---------------------------------------------
# Temel Kurallar:
# Python'da Class oluşturma:
# class ClassName: # PascalCase yapıda isimlendirilir.

#     variable_for_class = 'value'  # Atrribute/Property

#     # if (Conditions) ... # Wrong Using.

#     def example_function(paramatre, arguman):  # Method
         
#         variable_for_func = 'value'  # Parametre.

#         # if (Conditions)...
# ---------------------------------------------

# class Person:
#     name = 'Akif'
#     surname = 'Yilmaz'

# print(Person)
# print(Person.name)
# print(Person.surname)

# Set Object from Class:
# personel = Person() # Instance = Classtan oluşturulmuş obje.

# print(personel)
# print(personel.name)
# print(personel.surname)

# print('----------------')

# personel.name = 'Akif'
# personel.surname = 'Yilmaz'
# personel.age = 40

# print(personel.name)
# print(personel.surname)
# print(personel.age)

# print('----------------')

# print(Person.name)
# print(Person.surname)
# print(Person.age) # Instance'da yaptığımız değişkler class'ı ETKİLEMEZ.

# ---------------------------------------------

# Class'da yapılan değişiklikler Inctance'ı ETKİLER.
# class Person:
#     name = 'Akif'
#     surname = 'Yilmaz'

# personel_1 = Person()

# print(personel_1.name)
# Person.name = 'Akif'
# print(personel_1.name)

# ---------------------------------------------
# Bir instance'daki ekleme/güncelleme diğer instance'ı ETKİLEMEZ.
# class Person:
#     name = 'Akif'
#     surname = 'Yilmaz'

# personel_1 = Person()
# personel_2 = Person()

# print(personel_1)
# print(personel_2)

# personel_1.name = 'Akif'
# personel_2.name = 'Yilmaz'

# print(personel_1.name)
# print(personel_2.name)

# personel_1.age = 40

# print(personel_1.age)
# print(personel_2.age)

# ---------------------------------------------

# class Person:
#     name = 'Akif'
#     surname = 'Yilmaz'

# personel = Person # personel instance değil, class oldu.
# other_intance = personel() # Yeni class ile instance oluşturuldu.

# ---------------------------------------------

# class Person:

#     name = 'Akif'
#     surname = 'Yilmaz'

#     # this -> self
#     def test(self):
#         # this yerine self kullanıyoruz.
#         # self her zaman ilk argüman olmak zorunda.
#         # Instance'dan method çağırırken self parametresi yollamıyıyoruz.
#         print(self.name + ' ' + self.surname)

# personel = Person()
# personel.name = 'Akif'
# personel.surname = 'Yilmaz'
# personel.test() # Arka planda şu şekilde çalışır -> Person.test(personel)

# ---------------------------------------------
# Public / Private Attrs:

# class Person:

#     name = 'Akif'
#     surname = 'Yilmaz'
#     # Underscore ile başlayan değişkenlerin instance tarafında çağırlmaması/değiştirilmemesi beklenir.
#     # Piyasa standartıdır. Çağrılabilir.
#     _path = 'FS'
#     # Double-Underscore ile başlayan değişkenleri dışardan çağrılmasını engeller.
#     __location = 'Germany'


# personel = Person()
# print(personel.name)
# personel._path = 'AWS'
# print(personel._path) # Private attr'e erişim sağlanmaz.
# print(personel._Person__location) # Private attr'e ulaşmanın yolu.

# ---------------------------------------------
# Getter ve Setter Methodlar:

# class Person:

#     name = 'Akif'
#     surname = 'Yilmaz'
#     # Underscore ile başlayan değişkenlerin instance tarafında çağrılmaması/değiştirilmemesi beklenir.
#     # Piyasa standartıdır. Çağrılabilir.
#     _path = 'FS'
#     # Double-Underscore ile başlayan değişkenlerin dışardan çağrılmasını engeller.
#     __location = 'Germany'

#     def get_location(self):  # Getter Methods: get_ ile başlayan metodlar.
#         return self.__location

#     def set_location(self, new_val):  # Setter Methods: set_ ile başlayan metodlar.
#         self.__location = new_val

# personel = Person()
# print(personel.get_location())
# personel.set_location('Turkey')
# print(personel.get_location())

# class SendMail:

#     __is_sent = False

#     def send(self): # Setter Method.
#         # Mail gönderme komutları
#         # Mail gönderdikten sonra gönderildi bilgisini True yap.
#         self.__is_sent = True

#     def get_status(self): # Getter Method
#         # Mail gönderildi mi bilgisini ver.
#         return self.__is_sent

# mail = SendMail()
# print('Mail gönderildi mi?', mail.get_status()) # Bu bilgi hangi değişkenden olduğunu bilmiyoruz.
# mail.send()
# print('Mail gönderildi mi?', mail.get_status()) # Bu bilgi hangi değişkenden olduğunu bilmiyoruz.

# ---------------------------------------------
# Static Method:

# class Person:

#     name = 'Akif'
#     surname = 'Yilmaz'

#     @staticmethod
#     def test():
#         print('Hello')

#     @staticmethod
#     def hello(name, surname):
#         print('Hello ' + name + ' ' + surname)

# personel = Person()
# personel.test()
# personel.hello('Akif', 'Yilmaz')

# ---------------------------------------------
#Double-Underscore-Methods: DunderMethods:


class Person:
        
    name = 'Akif'
    surname = 'Yilmaz'
    
def __str__(self):
    return 'Benim yazdığım classtan üretilmiş intance/dir'

def ekrana_yaz(self):
    print(f'{self.name} {self.surname}')
    
def __init__(self):
    self.name = 'Mehmet'
    self.surname = 'Yılmaz'
    

    
    personal = Person()
    print(personal)
    personal.ekrana_yaz



