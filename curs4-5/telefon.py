# class Telefon:
#
#     counter = 0
#
#     def __init__(self, numar):
#         self.numar = numar
#         Telefon.counter += 1
#
#     def apelare(self, numar_apelat):
#         mesaj = f'Apelati {numar_apelat} folosind propriul numar'
#         return mesaj
#
#
# class TelefonFix(Telefon):
#
#     last_SN = 0
#
#     def __init__(self, numar):
#         super().__init__(numar)
#         TelefonFix.last_SN += 1
#         self.SN = f'TF - {TelefonFix.last_SN}'
#
#
# class TelefonMobil(Telefon):
#
#     last_SN = 0
#
#     def __init__(self, numar):
#         super().__init__(numar)
#         TelefonMobil.last_SN += 1
#         self.SN = f'TM - {TelefonMobil.last_SN}'
#
#
# print('Numarul total de deviceuri create', Telefon.counter)
# t1 = Telefon('0742 123 456')
# t2 = Telefon('0742 123 999')
#
# t3 = TelefonMobil('0742 563 456')
# t4 = TelefonMobil('0742 999 999')
# print(t4.SN)
# print('Numarul total de deviceuri create', Telefon.counter)
