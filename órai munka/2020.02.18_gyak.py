##gyakorlas##
# pelda:
#5 07:30 CEG300 590 30580 0
# #beolvasas
f = open("autok.txt", "r")
k = []
for i in f.readlines():
    l = i.strip().split(' ')
    n = int(l[0])
    o = l[1]
    r = str(l[2])
    sz = str(l[3])
    km = int(l[4])
    ha = int(l[5])
    k.append([n, o, r, sz, km, ha])
#print
# 2.feladat
napok2f = []
rendszam2f = []
for i in k:
    if i[5] == 0:
        napok2f.append(i[0])
        rendszam2f.append(i[2])


print(napok2f[-1], ". nap", "rendszam: ",rendszam2f[-1])

# 3.feladat
print("3. feladat")
bekeres = int(input("Nap: "))
tomb3f = []
for i in k:
    if i[0] == bekeres:
        if i[-1] == 0:
            i[-1] = 'ki'
        if i[-1] == 1:
            i[-1] = 'be'
        tomb3f.append(i)


print("Forgalom a(z)", bekeres, ". napon:")

for adatsor in tomb3f:
    print(adatsor[1], adatsor[2], adatsor[3], adatsor[-1])

"""
km = 1551
szem = 506.87654
print("Leghosszabb út: {0} km, személy: {1:6.2f}".format(km, szem))
# https://pyformat.info/
"""

# 4.feladat
szotar4f = {}
valtozo4f = 'valami'
for i in k:
    if i[2] in szotar4f:
        szotar4f[i[2]] = i[-1]
    else:
        szotar4f[i[2]] = i[-1]
print(szotar4f)

szamlalo = 0
for i in szotar4f:
    if szotar4f[i] == 0:
        szamlalo += 1

print("A hónap végén {} autót nem hoztak vissza.".format(szamlalo))

# 5 07:30 CEG300 590 30580 0
# 5.feladat
szotar5f = {}
szotar5f2 = {}
for i in k:
    if i[2] in szotar5f:
        None
    if i[2] not in szotar5f:
        szotar5f[i[2]] = i[4]

for i in k:
    if i[2] in szotar5f2:
        szotar5f2[i[2]] = i[4]
    else:
        szotar5f2[i[2]] = i[4]

for i in szotar5f2:
    szotar5f2[i] -= szotar5f[i]
    print("{0} {1} km".format(i, szotar5f2[i]))

"""
print("-----------------------")
for i in sorted(szotar5f2, reverse=True):
    szotar5f2[i] -= szotar5f[i]
    print("{0} {1} km".format(i ,szotar5f2[i]))
"""
"""
szotar5f = {}

for i in k:
    if not i[2] in szotar5f:
        szotar5f[i[2]] = []

    szotar5f[i[2]].append(i[4])

for i in szotar5f:
    print(i, max(szotar5f[i]) - min(szotar5f[i]), szotar5f[i])
"""