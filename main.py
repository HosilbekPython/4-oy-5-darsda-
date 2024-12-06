"""
Descriptorlar
"""
from bisect import insort


1 vazifa

class Deckriptor:
    def __set_name__(self, owner, name):
        self.name = name


    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name , None)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Qiymat faqat matn bo'lishi kerak!")
        if value.isdigit():
            print(f"{value} bu harfli matn emas!")
        else:
            instance.__dict__[self.name] = value.lower()

class Tekshirish:
    name = Deckriptor()
    def __init__(self , name):
        self.name = name


text = input("Soz kirirting : ")
p1 = Tekshirish(text)
print(p1.name)


# -------------------------------------------------------------------



# 2 vazifa


class RaqamgaTekshirish:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value:str):

        if value.isalpha():
            raise ValueError("Qiymat faqat raqam bo'lishi kerak!")
        else:
            instance.__dict__[self.name] = value

    def __delattr__(self, instance):
        del instance.__dict__[self.name]

class Tekshirish:
    raqam = RaqamgaTekshirish()

    def __init__(self , raqam):
        self.raqam  = raqam

raqam = input("Raqam kriting : ")
r1 = Tekshirish(raqam)
print(r1.raqam)







