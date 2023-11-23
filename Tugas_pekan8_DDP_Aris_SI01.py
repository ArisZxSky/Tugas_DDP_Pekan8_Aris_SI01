# Soal No 1
def profil (nama, alamat, gender, umur):
    print("nama saya adalah",nama)
    print("alamat saya di", alamat)
    print("gender saya", gender)
    print("umur saya", umur)
profil("Aris", "Bogor", "laki-laki", "20")


# Soal No 2
def keterangan_kelulusan(nilai):
    if nilai >= 0 and nilai <= 60:
        return "Gagal"
    elif nilai >= 61 and nilai <= 70:
        return "Baik"
    elif nilai >= 71 and nilai <= 80:
        return "Sangat Baik"
    elif nilai >= 81 and nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid!"
    
print(keterangan_kelulusan(75 ))


# Soal No 3
def bilangan_ganjil(n):
    for i in range(1, n+1, 2):
        print(i)
#pemanggilan
bilangan_ganjil(100)
