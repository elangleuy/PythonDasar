# Program Menghitung Gaji Karyawan Berdasarkan Flowchart
# Mulai
nama = input("Masukkan Nama: ")
gaji_pokok_str = input("Masukkan Gaji Pokok: ")
gaji_pokok = float(gaji_pokok_str)

# Proses Perhitungan
tunjangan = 0.20 * gaji_pokok
pajak = 0.15 * (gaji_pokok + tunjangan)
gaji_bersih = gaji_pokok + tunjangan - pajak

# Output
print(f"\nOutput:")
print(f"Nama: {nama}")
print(f"Gaji Pokok: {gaji_pokok}")
print(f"Gaji Bersih: {gaji_bersih}")
# Selesai