#2018
f = open("kerites.txt", "r")
k = []
paros = 2
paratlan = 1
for i in f.readlines():
    l = i.strip().split(' ')
    p = int(l[0])
    t = l[1]
    f = l[2]
    k.append([p, t, f])
length = 0
for i in k:
    if k[length][0] == 0:
        k[length].append(paros)
        paros += 2
    if k[length][0] == 1:
        k[length].append(paratlan)
        paratlan += 2
    length += 1

#2. feladat
print('2.Feladat')
print('Eladott telkek szama: ', length)

#3. feladat
print('3.Feladat')
if k[-1][0] == 0:
    print('A páros oldalon adták el az utolsó telket')
if k[-1][0] == 1:
    print('A páratlan oldalon adták el az utolsó telket')
print('Az utolsó telek házszáma:', k[-1][3])

#4.feladat
print('4.Feladat')
paratlanok = []
keritesek = 'x'
megoldas4 = 0
for i in k:
    if i[0] == 1:
        paratlanok.append(i)

for i in paratlanok:
    if keritesek == i[2]:
        if not i[2] == ':':
            if not i[2] == '#':
                megoldas4 = i[3]
                break
    keritesek = i[2]


print('A szomszédossal egyezik a kerítés színe: ', megoldas4)

#5.feladat
print('5.Feladat')
bekeres = int(input("Adjon meg egy házszámot! "))
valtozo1 = 0
szinvaltozo1 = 'x'
szinvaltozo2 = 'y'
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'J', 'K', 'L', 'M', 'N']
if not bekeres in k:
    print('Ilyen hazszam nincs!')
counter = 0
vnumber = 0
for i in k:
    if i[3] == bekeres:
        valtozo1 = i
        vnumber = counter
    counter += 1
print('A kerites szine: ', valtozo1[2])
z = vnumber - 1
c = vnumber + 1
j = '-'
for i in abc:
    if not k[vnumber][2] == i:
        if not k[z][2] == i:
            if not k[c][2] == i:
                j = i
                break
print('Egy lehetséges festési szin: ', j)



