import fisika

def batas():
    print("-"*15)

waktu_awal = time.time()

print( f"Massa Jenis = { fisika.MassaJenis.MassaJenis( 10, 2 )}")
print( f"Massa = { fisika.MassaJenis.Massa( 10, 2 )}")
print( f"Volume = { fisika.MassaJenis.Volume( 10, 2 )}")

waktu_akhir = time.time()
print( f" waktu yang dibutuhkan : { waktu_akhir - waktu_awal }")

batas()
print( f"usaha = { fisika.U( 12, 3 ) }")
print( f"Gaya = { fisika.G( 6, 2 ) } ")
print( f"Jarak = { fisika.J( 0.3 ) } ")

batas()

print( f" Hasil Energi Potensial : { }")