import itertools
import matplotlib.pyplot as plt
import time

# Fungsi untuk menghitung jarak total dari rute yang diberikan
def calculate_route_distance(route, distance_matrix):
    distance = 0
    for i in range(len(route) - 1):
        distance += distance_matrix[route[i]][route[i + 1]]
    distance += distance_matrix[route[-1]][route[0]]  # Kembali ke kota asal
    return distance

# Fungsi untuk mencari rute terpendek dengan backtracking
def find_shortest_route(distance_matrix):
    n = len(distance_matrix)
    shortest_distance = float('inf')
    shortest_route = None

    def backtrack(curr_route, curr_distance):
        nonlocal shortest_distance, shortest_route

        if len(curr_route) == n:
            curr_distance += distance_matrix[curr_route[-1]][curr_route[0]]  # Kembali ke kota asal
            if curr_distance < shortest_distance:
                shortest_distance = curr_distance
                shortest_route = curr_route[:]
            return

        for next_city in range(n):
            if next_city not in curr_route:
                backtrack(curr_route + [next_city], curr_distance + distance_matrix[curr_route[-1]][next_city])

    backtrack([0], 0)
    return shortest_route, shortest_distance

# Visualisasi rute terbaik menggunakan matplotlib
def plot_route(route, cities, coordinates):
    route_cities = [cities[i] for i in route] + [cities[route[0]]]  # Tambahkan kota awal di akhir rute
    x_coords = [coordinates[city][0] for city in route_cities]
    y_coords = [coordinates[city][1] for city in route_cities]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_coords, y_coords, marker='o')
    for i, city in enumerate(route_cities):
        plt.text(x_coords[i], y_coords[i], city)
    plt.xlabel('Koordinat X')
    plt.ylabel('Koordinat Y')
    plt.title('Rute Terbaik untuk Distribusi Barang')
    plt.grid()
    plt.show()

# Fungsi untuk menghitung biaya bahan bakar berdasarkan jarak
def calculate_fuel_cost(distance, fuel_price_per_liter, fuel_efficiency):
    return (distance / fuel_efficiency) * fuel_price_per_liter

# Data contoh untuk jarak antar kota di sekitar Bandung (distance matrix)
distance_matrix = [
    #   Lembang, Bandung, Cimahi, Sumedang, Soreang, Banjaran, Cileunyi, Majalaya
    [0, 13, 11, 39, 29, 32, 27, 35],    # Lembang
    [13, 0, 10, 32, 18, 22, 15, 25],    # Bandung
    [11, 10, 0, 38, 18, 21, 17, 27],    # Cimahi
    [39, 32, 38, 0, 50, 50, 23, 30],    # Sumedang
    [29, 18, 18, 50, 0, 15, 30, 25],    # Soreang
    [32, 22, 21, 50, 15, 0, 35, 28],    # Banjaran
    [27, 15, 17, 23, 30, 35, 0, 10],    # Cileunyi
    [35, 25, 27, 30, 25, 28, 10, 0]     # Majalaya
]

# Koordinat kota untuk visualisasi (acak untuk tujuan plotting)
coordinates = {
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
start_time = time.time()

# Memanggil fungsi untuk mencari rute terpendek menggunakan backtracking
best_route, min_distance = find_shortest_route(distance_matrix)

# Mengukur waktu eksekusi
end_time = time.time()
execution_time = end_time - start_time

# Harga bahan bakar dan efisiensi kendaraan
fuel_price_per_liter = 10000  # contoh harga bahan bakar (Rp per liter)
fuel_efficiency = 12  # contoh efisiensi bahan bakar (km per liter)

# Menghitung biaya bahan bakar
total_fuel_cost = calculate_fuel_cost(min_distance, fuel_price_per_liter, fuel_efficiency)

# Ekstraksi nama kota dari koordinat
cities = {
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
best_route = best_route + [best_route[0]]

# Ubah angka menjadi nama kota
best_route_named = [cities[i] for i in best_route]

print(f"Rute terbaik: {best_route_named}")
print(f"Jarak terpendek: {min_distance} km")
print(f"Biaya bahan bakar: Rp {total_fuel_cost}")
print(f"Waktu eksekusi: {execution_time} detik")

# Visualisasikan rute terbaik
plot_route(best_route, cities, coordinates)