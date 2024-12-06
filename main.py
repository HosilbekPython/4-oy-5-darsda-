"""
Datetime Moduli
"""

# 1 vazifa

#
# from datetime import date ,datetime , timedelta
#
#
# class Datani_olish:
#     def bugungi_sana(self):
#         bugungi_sana = date.today()
#         return bugungi_sana
#
#     def yetti_kun_oldin(self):
#         yeti = timedelta(days=7)
#         bugungi_sana = date.today()
#         return bugungi_sana - yeti
#
#     def yetti_kun_keyin(self):
#         yeti = timedelta(days=7)
#         bugungi_sana = date.today()
#         return bugungi_sana + yeti
#
# sana = Datani_olish()
# print(sana.bugungi_sana())
# print(sana.yetti_kun_oldin())
# print(sana.yetti_kun_keyin())



# 2 vazifa


# from datetime import date ,datetime , timedelta
#
# class Tugulgan_kun_qoldi:
#     def __init__(self , sana_str):
#         self.sana_str = sana_str
#
#     def sana_string_to_date(self):
#         sana = datetime.strptime(self.sana_str , "%d-%m-%Y")
#         bugun = datetime.now()
#         if sana.replace(year=bugun.year) < bugun:
#             sana = sana.replace(year=bugun.year + 1)
#
#         else:
#             sana = sana.replace(year=bugun.year)
#
#         qoldi = sana - bugun
#         if qoldi.days == 364:
#             return "Tugulgan kunigiz bilan 🔥🔥 "
#         else:
#             return f"{qoldi.days} kun "
# tugulgan_kun = input("Tugulgan kunigizni yuboring (dd-mm-YYYY) : ")
# kun1 = Tugulgan_kun_qoldi(tugulgan_kun)
# print(kun1.sana_string_to_date())





# 3 vazifa

# import time
#
#
# time1 = "12:10:00"
# time2 = "12:10:50"
#
# timee1 = time.strptime(time1 , "%H:%M:%S")
# timee2 = time.strptime(time2 , "%H:%M:%S")
#
# time1_sec = timee1.tm_hour * 3600 + timee1.tm_min * 60 + timee1.tm_sec
# time2_sec = timee2.tm_hour * 3600 + timee2.tm_min * 60 + timee2.tm_sec
#
# farqi = time2_sec - time1_sec
#
# print(farqi)







