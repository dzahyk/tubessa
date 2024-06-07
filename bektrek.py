import matplotlib.pyplot as plt
import time

# Fungsi untuk menghitung jarak total dari rute yang diberikan
def hitung_jarak_rute(rute, matriks_jarak):
    jarak = 0
    for i in range(len(rute) - 1):
        jarak += matriks_jarak[rute[i]][rute[i + 1]]
    jarak += matriks_jarak[rute[-1]][rute[0]]  # Kembali ke kota asal
    return jarak

# Fungsi untuk mencari rute terpendek dengan backtracking
def cari_rute_terpendek(matriks_jarak):
    n = len(matriks_jarak)
    jarak_terpendek = float('inf')
    rute_terpendek = None

    def backtrack(rute_saat_ini, jarak_saat_ini):
        nonlocal jarak_terpendek, rute_terpendek

        if len(rute_saat_ini) == n:
            jarak_saat_ini += matriks_jarak[rute_saat_ini[-1]][rute_saat_ini[0]]  # Kembali ke kota asal
            if jarak_saat_ini < jarak_terpendek:
                jarak_terpendek = jarak_saat_ini
                rute_terpendek = rute_saat_ini[:]
            return

        for kota_berikutnya in range(n):
            if kota_berikutnya not in rute_saat_ini:
                backtrack(rute_saat_ini + [kota_berikutnya], jarak_saat_ini + matriks_jarak[rute_saat_ini[-1]][kota_berikutnya])

    backtrack([0], 0)
    return rute_terpendek, jarak_terpendek

# Visualisasi rute terbaik menggunakan matplotlib
def plot_rute(rute, kota, koordinat):
    rute_kota = [kota[i] for i in rute] + [kota[rute[0]]]  # Tambahkan kota awal di akhir rute
    x_koordinat = [koordinat[city][0] for city in rute_kota]
    y_koordinat = [koordinat[city][1] for city in rute_kota]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_koordinat, y_koordinat, marker='o')
    for i, city in enumerate(rute_kota):
        plt.text(x_koordinat[i], y_koordinat[i], city)

    # Tambahkan panah untuk menunjukkan arah rute
    for i in range(len(rute_kota) - 1):
        plt.annotate(
            '', xy=(x_koordinat[i+1], y_koordinat[i+1]), xytext=(x_koordinat[i], y_koordinat[i]),
            arrowprops=dict(facecolor='blue', shrink=0.05)
        )
    # Tambahkan panah dari kota terakhir kembali ke kota asal
    plt.annotate(
        '', xy=(x_koordinat[0], y_koordinat[0]), xytext=(x_koordinat[-1], y_koordinat[-1]),
        arrowprops=dict(facecolor='blue', shrink=0.05)
    )

    plt.xlabel('Koordinat X')
    plt.ylabel('Koordinat Y')
    plt.title('Rute Terbaik untuk Distribusi Barang')
    plt.grid()
    plt.show()

# Fungsi untuk menghitung biaya bahan bakar berdasarkan jarak
def hitung_biaya_bahan_bakar(jarak, harga_bahan_bakar_per_liter, efisiensi_bahan_bakar):
    return (jarak / efisiensi_bahan_bakar) * harga_bahan_bakar_per_liter

# Data jarak antar kota di sekitar Bandung berdasarkan Google Map (matriks jarak)
matriks_jarak = [
    #   Lembang, Bandung, Cimahi, Sumedang, Soreang, Banjaran, Cileunyi, Majalaya
    [0, 14, 20, 56, 32, 32, 27, 42],    # Lembang
    [14, 0, 13, 46, 18, 20, 18, 26],    # Bandung
    [20, 13, 0, 58, 22, 28, 30, 35],    # Cimahi
    [56, 46, 58, 0, 60, 57, 31, 40],    # Sumedang
    [32, 18, 22, 60, 0, 8, 31, 31],     # Soreang
    [32, 20, 28, 57, 8, 0, 28, 23],     # Banjaran
    [27, 18, 30, 31, 31, 28, 0, 19],    # Cileunyi
    [42, 26, 35, 40, 31, 23, 19, 0]     # Majalaya
]

# Koordinat kota untuk visualisasi (acak untuk tujuan plotting)
koordinat = {
    "Lembang": (10, 60),
    "Bandung": (20, 50),
    "Cimahi": (15, 45),
    "Sumedang": (50, 50),
    "Soreang": (30, 30),
    "Banjaran": (35, 25),
    "Cileunyi": (40, 60),
    "Majalaya": (45, 40)
}

# Mengukur waktu eksekusi
waktu_mulai = time.time()

# Memanggil fungsi untuk mencari rute terpendek menggunakan backtracking
rute_terbaik, jarak_terpendek = cari_rute_terpendek(matriks_jarak)

# Mengukur waktu eksekusi
waktu_selesai = time.time()
waktu_eksekusi = waktu_selesai - waktu_mulai

# Harga bahan bakar dan efisiensi kendaraan
harga_bahan_bakar_per_liter = 10000  # contoh harga bahan bakar (Rp per liter)
efisiensi_bahan_bakar = 12  # contoh efisiensi bahan bakar (km per liter)

# Menghitung biaya bahan bakar
total_biaya_bahan_bakar = hitung_biaya_bahan_bakar(jarak_terpendek, harga_bahan_bakar_per_liter, efisiensi_bahan_bakar)

# Ekstraksi nama kota dari koordinat
kota = {
    0: "Lembang",
    1: "Bandung",
    2: "Cimahi",
    3: "Sumedang",
    4: "Soreang",
    5: "Banjaran",
    6: "Cileunyi",
    7: "Majalaya"
}

# Tambahkan kembali titik awal ke rute terpendek
rute_terbaik = rute_terbaik + [rute_terbaik[0]]

# Ubah angka menjadi nama kota
rute_terbaik_bernama = [kota[i] for i in rute_terbaik]

print(f"Rute terbaik: {rute_terbaik_bernama}")
print(f"Jarak terpendek: {jarak_terpendek} km")
print(f"Biaya bahan bakar: Rp {total_biaya_bahan_bakar}")
print(f"Waktu eksekusi: {waktu_eksekusi} detik")

# Visualisasikan rute terbaik
plot_rute(rute_terbaik, kota, koordinat)
