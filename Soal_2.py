tahun = int(input('Masukkan Tahun : '))
if tahun % 4 == 0 and tahun % 100 != 0 or tahun % 400 == 0:
    print(f'Tahun {tahun} merupakan TAHUN KABISAT')
else:
    print(f'Tahun {tahun} Bukan TAHUN KABISAT')