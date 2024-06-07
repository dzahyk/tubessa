import timeit
import matplotlib.pyplot as plt

# Mendefinisikan nama kota dan koordinat kota (x, y)
nama_kota = ["Lembang", "Bandung", "Cimahi", "Sumedang", "Soreang", "Banjaran", "Cileunyi", "Majalaya"]
koordinat_kota = {
    "Lembang": (10, 60),
    "Bandung": (20, 50),
    "Cimahi": (15, 45),
    "Sumedang": (50, 50),
    "Soreang": (30, 30),
    "Banjaran": (35, 25),
    "Cileunyi": (40, 60),
    "Majalaya": (45, 40)
}

# Mencari kota terdekat yang belum dikunjungi
def kotaTerdekat(kota, jarak, visited):
    jarakMinimal = 1000
    nearest_city = None
    for kotaTujuan in range(len(jarak)):
        if not visited[kotaTujuan] and jarak[kota][kotaTujuan] < jarakMinimal:
            jarakMinimal = jarak[kota][kotaTujuan]
            nearest_city = kotaTujuan
    return nearest_city, jarakMinimal

# Greedy
def ruteGreedy(distances, bensinAwal):
    jumlahKota = len(distances)
    visited = [False] * jumlahKota
    currentCity = 0
    rute = [currentCity]
    jarakTotal = 0
    fuel = bensinAwal
    costBensin = 0
    hargaperLiter = 10000
    konsumsiBensinPerKm = 1 / 12

    visited[currentCity] = True

    for _ in range(jumlahKota - 1): #menggunakan _ karena variabel iterasi tidak digunakan dalam loop
        nextCity, distance = kotaTerdekat(currentCity, distances, visited)
        if nextCity is None:
            print("Tidak ada kota yang dapat dikunjungi lagi.")
            return rute, jarakTotal, fuel, int(costBensin)
        
        rute.append(nextCity)
        jarakTotal += distance
        fuel -= distance * konsumsiBensinPerKm
        costBensin += distance * hargaperLiter * konsumsiBensinPerKm
        if fuel < 0:
            print("Bahan bakar habis sebelum mencapai semua kota.")
            return rute, jarakTotal, 0, int(costBensin)
        
        visited[nextCity] = True
        currentCity = nextCity

    # Kembali ke kota awal
    jarakTotal += distances[currentCity][0]
    rute.append(0)
    fuel -= distances[currentCity][0] * konsumsiBensinPerKm
    costBensin += distances[currentCity][0] * hargaperLiter * konsumsiBensinPerKm
    if fuel < 0:
        print("Bahan bakar habis sebelum kembali ke kota awal.")
        return rute, jarakTotal, 0, int(costBensin)

    return rute, jarakTotal, fuel, int(costBensin)

# Contoh data jarak antar kota (matriks) yang lebih banyak
distances = [
    [0, 14, 20, 56, 32, 32, 27, 42],    # Lembang
    [14, 0, 13, 46, 18, 20, 18, 26],    # Bandung
    [20, 13, 0, 58, 22, 28, 30, 35],    # Cimahi
    [56, 46, 58, 0, 60, 57, 31, 40],    # Sumedang
    [32, 18, 22, 60, 0, 8, 31, 31],    # Soreang
    [32, 20, 28, 57, 8, 0, 28, 23],    # Banjaran
    [27, 18, 30, 31, 31, 28, 0, 19],    # Cileunyi
    [42, 26, 35, 40, 31, 23, 19, 0]     # Majalaya
]

# Nilai awal bahan bakar
initialFuel = 100

# Fungsi untuk menjalankan algoritma greedy
def runGreedyrute():
    return ruteGreedy(distances, initialFuel)

executionTime = timeit.timeit(runGreedyrute, number=1)

route, totalDistance, sisaBensin, harga = runGreedyrute()

route_with_names = [nama_kota[i] for i in route]

print("Rute yang diambil:", route_with_names)
print("Jarak total yang ditempuh:", totalDistance, "Km")
print("Sisa bahan bakar:", sisaBensin)
print("Total biaya bahan bakar:", harga, "rupiah")
print("Waktu eksekusi: {:.10f} detik".format(executionTime))

# Visualisasi graf rute
def visualize_route(route, koordinat_kota, nama_kota):
    fig, ax = plt.subplots()
    x_coords = [koordinat_kota[nama_kota[i]][0] for i in route]
    y_coords = [koordinat_kota[nama_kota[i]][1] for i in route]
    
    for i in range(len(route) - 1):
        start = route[i]
        end = route[i + 1]
        start_x, start_y = koordinat_kota[nama_kota[start]]
        end_x, end_y = koordinat_kota[nama_kota[end]]
        ax.annotate("",
                    xy=(end_x, end_y), xycoords='data',
                    xytext=(start_x, start_y), textcoords='data',
                    arrowprops=dict(arrowstyle="->",
                                    connectionstyle="arc3"))

    for i, kota in enumerate(route):
        x, y = koordinat_kota[nama_kota[kota]]
        ax.annotate(nama_kota[kota], (x, y), textcoords="offset points", xytext=(0,10), ha='center')
        ax.plot(x, y, 'bo')
    
    ax.set_title('Rute yang Diambil')
    ax.set_xlabel('Koordinat X')
    ax.set_ylabel('Koordinat Y')
    plt.grid(True)
    plt.show()

route_indices = [nama_kota.index(kota) for kota in route_with_names]

# Visualisasikan rute
visualize_route(route_indices, koordinat_kota, nama_kota)
