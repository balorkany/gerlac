#2019_okt.
#0 20190326-0700 6915170 FEB 20210101
#1.feladat
f = open("utasadat.txt", "r")
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