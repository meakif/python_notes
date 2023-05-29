import os
os.system('cls' if os.name=="nt" else 'clear')
# ---------------------------------------------
# ---------------------------------------------
# Python - OOP - 2
# ---------------------------------------------
#Encapcullation:Kapsülleme. Aynı amaç için kullanılan değişken methodları bir class içinde yazıyor olmamız örnektir.
#Abstraction:   Soyutlama. Kodların gizliliği veya birbirinden bağımsız çalışmaları.


class Person:
    company = 'Clarusway'
    
    def __init__(self, name, age, gender='Male'):
        self.name = name 
        self.age = age
        self.gender = gender
        print('Personel oluşturuldu.')
        
    def __str__(self):
        return f'{self.name} - {self.age}'
    
    def get_detail(self):
        return f'{self.name} - {self.age} - {self.gender} - {self.company}'
    
# person_1 = Person('Akif' , 23) 
#Bir classın atandığı değişkene intance denir.
#print(person_1)
#print(person_1.get_detail())

#İngeritance
class Employee(Person): #Person classın tüm özellikleri employe classına aktarıldı.
    
    salary = 5000
    
    def set_salary(self, salary):
        self.salary = salary
        
    def get_detail(self):
        return f'{self.name} - {self.age} - {self.gender} - {self.company} - {self.salary}'
    
    
person_1 = Employee('Gamze', 22, 'Female') 
person_1.salary = 2000
print(person_1.get_detail())

