n = int(input("Masukkan jumlah baris: "))

for i in range(1, n + 1):
    # spasi di sebelah kiri
    for j in range(n - i):
        print(" ", end="")
    # bintang dengan spasi
    for k in range(i):
        print("* ", end="")
    print()