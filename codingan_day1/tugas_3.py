while True:
    try:
        nilai_siswa = int(input("input nilai_siswa: "))
        if nilai_siswa >= 75:
            print("Tuntas")
            break # End program flow if Tuntas
        else:
            mengulang = input("input mengulang (Ya/Tidak): ")
            if mengulang == "Ya":
                continue # Loop back to ask for nilai_siswa
            else:
                print("Tidak Tuntas")
                break # End program flow if Tidak Tuntas
    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk nilai siswa.")