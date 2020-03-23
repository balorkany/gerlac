#2013
#09 20 15 ZA-9745
#1. feladat
f = open("jarmu.txt", "r")
k = []
for i in f.readlines():
    l = i.strip().split(' ')
    o = int(l[0])
    p = int(l[1])
    m = int(l[2])
    r = l[3]
    I = o*3600 + p*60 + m
    k.append([o, p, m, r, I])
print(k)
#2. feladat
print('2.feladat')
fel2a = k[0][0]*3600 + k[0][1]*60 + k[0][2]
fel2b = k[-1][0]*3600 + k[-1][1]*60 + k[-1][2]
fel2c = fel2b - fel2a
fel2d = fel2c//3600
fel2f = fel2c//60 - fel2d*60
fel2e = fel2c - (fel2d*3600 + fel2f*60)
if fel2e < 0:
    fel2e = fel2e*-1
    fel2e = 60 - fel2e
    fel2f = fel2f - 1
if fel2f < 0:
    fel2f = fel2f*-1
    fel2f = 60 - fel2f
    fel2d = fel2d - 1
#print(fel2c)
print("{0}.óra {1}.perc {2}.masodperc".format(fel2d, fel2f, fel2e))

#3. feladat
print("3.feladat")
fel3 = {}
for i in k:
    if not i[0] in fel3:
        fel3[i[0]] = i[3]
for i in fel3:
    print("{0}.óra: {1}".format(i, fel3[i]))
    #print("{0} óra: {1}".format(fel3[i][0], fel3[i]))

#4. feladat
print("4.feladat")
print(k[1][3][0:1])
K = 0
B = 0
G = 0
M = 0
for i in k:
    if str(i[3][0:1]) == 'K':
        K += 1
    if str(i[3][0:1]) == 'B':
        B += 1
    if str(i[3][0:1]) == 'M':
        M += 1
    if not str(i[3][0:1]) == 'B' and 'K' and 'M':
        G += 1
print("K: ", K)
print("B: ", B)
print("G: ", G)
print("M: ", M)

#5.feladat
print("5.feladat")
elozo = k[2][4]
nagyobb = 0
gyujtes1 = 0
gyujtes2 = 0
for i in k:
    a = i[4] - elozo
    if a >= nagyobb:
        nagyobb = a
        gyujtes1 = i[4]
        gyujtes2 = elozo
    elozo = i[4]
x5 = []
y5 = []
for i in k:
    if i[4] == gyujtes1:
       x5 = (i[0], i[1], i[2])
    if i[4] == gyujtes2:
        y5 =(i[0], i[1], i[2])
print("{0}:{1}:{2}-{3}:{4}:{5}".format(y5[0], y5[1], y5[2], x5[0], x5[1], x5[2]))

#6.feladat
print("6.feladat")
bekeres = input("Egy rendszamot kerek: ")
csillag = 0
if bekeres[0] == '*':
    csillag += 1
if bekeres[1] == "*":
    csillag += 1
if bekeres[3] == "*":
    csillag += 1
if bekeres[4] == "*":
    csillag += 1
if bekeres[5] == "*":
    csillag += 1
if bekeres[6] == "*":
    csillag += 1
betuk = 6 - csillag
x = 0
rendszamok = []
print(csillag)
for i in k:
    if not i[3][0] == '*':
        if i[3][0] == bekeres[0]:
            x += 1
    if not i[3][1] == '*':
        if i[3][1] == bekeres[1]:
            x += 1
    if not i[3][3] == '*':
        if i[3][3] == bekeres[3]:
            x += 1
    if not i[3][4] == '*':
        if i[3][4] == bekeres[4]:
            x += 1
    if not i[3][5] == '*':
        if i[3][5] == bekeres[5]:
            x += 1
    if not i[3][6] == '*':
        if i[3][6] == bekeres[6]:
            x += 1
    if x == betuk:
        rendszamok.append(i[3])
    x = 0
print(rendszamok)

#7.feladat
print("7.feladat")
ki_file = open("vizsgalt.txt", 'w')
elozo7 = k[1][4]
feladatmegoldas = []
c = 0
for i in k:
    c += i[4] - elozo7
    print(c)
    if c == 300:
        c = 0
        feladatmegoldas.append(i)
    elozo7 = i[4]

'''
for i in gyujto:
    print("{0} {1}".format(i, gyujto[i]))
'''
print(feladatmegoldas)
for i in feladatmegoldas:
    ki_file.write(i)

ki_file.close()
