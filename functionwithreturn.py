def penjumlahan(x,y):
    result = x+y
    return result

hitung = penjumlahan(129,700)
print('Hasil penjumlahan adalah = ', hitung)

def hitungluas(panjang, lebar):
    return (panjang*lebar)

print("Luas persegi adalah: ", hitungluas(100,50))

def harga_setelah_pajak(hargadasar):
    return hargadasar + (hargadasar * 10/100)

harga_es_buah = 10000
harga_final_es_buah = harga_setelah_pajak(harga_es_buah)
print('harga es buah 1 porsi Rp.',harga_final_es_buah)

def my_function(x):
    return x * 5

print(my_function(6))
print(my_function(7))
print(my_function(10))

def nama(depan):
    print(depan+ " Joni")

nama("Alberty")
nama("John")
nama("Miguel")