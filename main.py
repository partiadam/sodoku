import math
from random import choice

class Feladvany:
   
    def __init__(self, sor):
    
        self.kezdo = sor
        self.meret = int(math.sqrt(len(sor)))
    

    def kirajzol(self):
        for i in range(len(self.kezdo)):
            if (self.kezdo[i] == '0'):
                print(".", end="")            
            else:
                print(self.kezdo[i], end="")
            
            if (i % self.meret == self.meret - 1):
                print()
            


lista = []
with open('feladvanyok.txt')as f:
    for sor in f:
        lista.append(Feladvany( sor.strip() ))

#3. feladat
        
print(f'3. feladat: Beolvasva {len(lista)} feladvány.')

#4. feladat
while True:
    beker = int(input('Kérem a feladvány méretét: [4..9]: '))
    if 4 <= beker <= 9:
        break
'''
szamlalo = 0
for feladat in lista:
    if feladat.meret == beker:
        szamlalo += 1
'''
feladatok =  [feladat for feladat in lista if feladat.meret == beker ]
szamlalo = len(feladatok)
print(f'{beker}x{beker} méretű feladványból {szamlalo} darab van tárolva.')
    

#5. feladat

feladat = choice(feladatok)
print(f'5. feladat: A kiválasztott feladvány: ')
print(feladat.kezdo)

#6. feladat

nemnulla = 0
for karakter in feladat.kezdo:
    if karakter != '0':
        nemnulla += 1

szazalek = nemnulla / len(feladat.kezdo) * 100
print(f'6. feladat: A feladvány kitöltöttsége: {szazalek:.0f}%.')    

#7. feladat

print('7. feladat: A feladvány kirajzolva: ')
feladat.kirajzol()