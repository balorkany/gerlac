#2019_okt.
#0 20190326-0700 6915170 FEB 20210101

"""
Függvény napokszama(e1:egész, h1:egész, n1: egész, e2:egész, h2: egész, n2: egész): egész
	h1 = (h1 + 9) MOD 12
	e1 = e1 - h1 DIV 10
	d1= 365*e1 + e1 DIV 4 - e1 DIV 100 + e1 DIV 400 + (h1*306 + 5) DIV 10 + n1 - 1
	h2 = (h2 + 9) MOD 12
	e2 = e2 - h2 DIV 10
	d2= 365*e2 + e2 DIV 4 - e2 DIV 100 + e2 DIV 400 + (h2*306 + 5) DIV 10 + n2 - 1
	napokszama:= d2-d1
Függvény vége
"""


def napokszama(e1, h1, n1, e2, h2, n2):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365 * e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1 * 306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2 = 365 * e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2 * 306 + 5) // 10 + n2 - 1

    return d2 - d1

#1.feladat
f = open("utasadat.txt", "r")
#f = open("ua.txt", "r")
k = []
for i in f.readlines():
    l = i.strip().split(' ')
    m = l[0]
    d = l[1].split('-')
    int(d[0])
    int(d[1])
    sz = l[2]
    b = l[3]
    a = int(l[4])
    k.append([m, d, sz, b, a])
print(k[5])

#2.feladat
print("2. feladat")
print('A buszra', len(k),'utas akart felszallni.')

#3.feladat
print("3. feladat")
szamlalo3 = 0
for i in k:
    if int(i[1][0]) > i[4]:
        if i[4] > 200 or i[4] == 0:
            szamlalo3 += 1
print('A buszra', szamlalo3, 'utas nem szallhatott fel.')

#4.feladat
print("4. feladat")
szotar = {}
atmenet = {}
for i in k:
    if i[0] in szotar:
        szotar[i[0]] += 1
    if not i[0] in szotar:
        szotar[i[0]] = 1

atmenet = max(zip(szotar.values(), szotar.keys())) # <-------------- lehet ezt mashogy ?
print("A legtöbb utas ( {0} fő ) a {1}. - ik megallonal szallt le".format(atmenet[0], atmenet[1]))

max_megallo = 0
max_felszallo = 0

for m in szotar:
    if max_felszallo < szotar[m]:
        max_megallo = m
        max_felszallo = szotar[m]

print(max_megallo, max_felszallo)

#5.feladat
print("5. feladat")
ingyenes = 0
kedvezmenyes = 0
for i in k:
    if i[3] == 'NYP':
        ingyenes += 1
    if i[3] == 'RVS':
        ingyenes += 1
    if i[3] == 'GYK':
        ingyenes += 1
    if i[3] == 'TAB':
        kedvezmenyes += 1
    if i[3] == 'NYB':
        kedvezmenyes += 1
print("Ingyenesen utazok szama: ", ingyenes, 'fo')
print("kedvezmenyesen utazok szama: ", kedvezmenyes, "fo")


# 6. feladat

# 7. feladat

ki_file = open("figyelmeztetes.txt", 'w')

gyujto = {}
#0 20190326-0700 3812852 NYB 20190413
#def napokszama(e1, h1, n1, e2, h2, n2):
e1 = int(k[0][1][0][0:4])
h1 = int(k[0][1][0][4:6])
n1 = int(k[0][1][0][6:8])

for i in k:
    if not i[3] == 'JGY':
        e2 = int(str(i[4])[0:4])
        h2 = int(str(i[4])[4:6])
        n2 = int(str(i[4])[6:8])
        if napokszama(e1, h1, n1, e2, h2, n2) <= 3:
            gyujto[i[2]] = ("{0}-{1}-{2}".format(e2, h2, n2))
'''
for i in gyujto:
    print("{0} {1}".format(i, gyujto[i]))
'''
for i in gyujto:
    ki_file.write("{0} {1} \n".format(i, gyujto[i]))

ki_file.close()
