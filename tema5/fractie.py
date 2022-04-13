class Fractie:

    def __init__(self, numa, numi):
        self.numa = numa
        self.numi = numi

    def __str__(self):
        return f'numarator/numitor: {self.numa}/{self.numi}'

    def __add__(self, otherfunction):
        new_numa = self.numa * otherfunction.numi + self.numi * otherfunction.numa
        new_numi = self.numi * otherfunction.numi
        return f'{new_numa}/{new_numi}'

    def __sub__(self, otherfunction):
        new_numa = self.numa * otherfunction.numi - self.numi * otherfunction.numa
        new_numi = self.numi * otherfunction.numi
        return f'{new_numa}/{new_numi}'

    def inversa(self):
        aux = self.numi
        self.numi = self.numa
        self.numa = aux
        return f'{self.numa}/{self.numi}'


f1 = Fractie(14, 15)
print(f1)
f2 = Fractie(13, 12)
f3 = f1 + f2
print(f3)
f4 = f1 - f2
print(f4)
f5 = f1.inversa()
print(f5)