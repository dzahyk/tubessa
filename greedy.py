import timeit

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

    visited[currentCity] = True

    for _ in range(jumlahKota - 1): #menggunakan _ karena variabel iterasi tidak digunakan dalam loop
        nextCity, distance = kotaTerdekat(currentCity, distances, visited)
        if nextCity is None:
            print("Tidak ada kota yang dapat dikunjungi lagi.")
            return rute, jarakTotal, fuel, costBensin
        
        rute.append(nextCity)
        jarakTotal += distance
        fuel -= distance
        costBensin += distance * hargaperLiter
        if fuel < 0:
            print("Bahan bakar habis sebelum mencapai semua kota.")
            return rute, jarakTotal, 0, costBensin
        
        visited[nextCity] = True
        currentCity = nextCity

    # Kembali ke kota awal
    jarakTotal += distances[currentCity][0]
    rute.append(0)
    fuel -= distances[currentCity][0]
    costBensin += distances[currentCity][0] * hargaperLiter
    if fuel < 0:
        print("Bahan bakar habis sebelum kembali ke kota awal.")
        return rute, jarakTotal, 0, costBensin

    return rute, jarakTotal, fuel, costBensin

# Contoh data jarak antar kota (matriks) yang lebih banyak
distances = [
    [0, 13, 11, 39, 29, 32, 27, 35],    # Lembang
    [13, 0, 10, 32, 18, 22, 15, 25],    # Bandung
    [11, 10, 0, 38, 18, 21, 17, 27],    # Cimahi
    [39, 32, 38, 0, 50, 50, 23, 30],    # Sumedang
    [29, 18, 18, 50, 0, 15, 30, 25],    # Soreang
    [32, 22, 21, 50, 15, 0, 35, 28],    # Banjaran
    [27, 15, 17, 23, 30, 35, 0, 10],    # Cileunyi
    [35, 25, 27, 30, 25, 28, 10, 0]     # Majalaya
]

# Nilai awal bahan bakar
initial_fuel = 1000

# Membungkus pemanggilan fungsi greedy_route dalam sebuah fungsi
def runGreedyrute():
    return ruteGreedy(distances, initial_fuel)

# Mengukur waktu eksekusi menggunakan timeit
execution_time = timeit.timeit(runGreedyrute, number=1)

# Jalankan algoritma greedy
route, totalDistance, sisaBensin, harga = runGreedyrute()

print("Rute yang diambil:", route)
print("Jarak total yang ditempuh:", totalDistance)
print("Sisa bahan bakar:", sisaBensin)
print("Total biaya bahan bakar:", harga, "rupiah")
print("Waktu eksekusi: {:.10f} detik".format(execution_time))
