jumlah_barang = int(input('Masukan Jumlah Barang : '))

harga_barang_awal = 0
for barang in range (1, jumlah_barang +1):
    harga_barang = int(input(f'Masukan Harga Barang Ke {barang} : '))
    harga_barang_awal += harga_barang
total = harga_barang_awal
print(f"Total Belanjaan : ",total)