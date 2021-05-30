# Function dengan Parameter dan Argumen
# Parameter adalah sebuah variabel yang ada di dalam function
# Argumen adalah sebuah nilai yang ada di dalam function ketika di panggil

# syntax penulisan nya:
# def function(param1,param2):
# blok kode/isi
# function(args1,args2)

# def penjumlahan(angka1, angka2,angka3):
   # print("Ini adalah angka 1 dan angka 2 = ", angka1, angka2,angka3)

#penjumlahan(10,7,466)
#penjumlahan(15,27,100)
#penjumlahan(113,490,100)

def perkalian(x, y):
    result = x*y
    print('Hasil perkalian adalah =', result)

perkalian(10,10)
perkalian(16,1453)

def pembagian(x, y):
    result = x/y
    print('Hasil pembagian adalah =', result)

pembagian(100,10)
pembagian(200,4)

def penjumlahan(x,y):
    result = x+y
    print('Hasil penjumlahan adalah = ', result)

penjumlahan(129,700)
penjumlahan(199,888)

def pengurangan(x,y):
    result = x-y
    print('Hasil pengurangan adalah = ', result)

pengurangan(999, 77)
pengurangan(16, 77)

def penggabungan(angka1, angka2, angka3, angka4):
    result = angka1*angka2+angka3/angka4
    print('Hasil dari penggabungan = ', result)

penggabungan(150, 245, 127, 50)


