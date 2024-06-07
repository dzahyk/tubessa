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

    # Tambahkan panah untuk menunjukkan arah rute
    for i in range(len(route_cities) - 1):
        plt.annotate(
            '', xy=(x_coords[i+1], y_coords[i+1]), xytext=(x_coords[i], y_coords[i]),
            arrowprops=dict(facecolor='blue', shrink=0.05)
        )
    # Tambahkan panah dari kota terakhir kembali ke kota asal
    plt.annotate(
        '', xy=(x_coords[0], y_coords[0]), xytext=(x_coords[-1], y_coords[-1]),
        arrowprops=dict(facecolor='blue', shrink=0.05)
    )

    plt.xlabel('Koordinat X')
    plt.ylabel('Koordinat Y')
    plt.title('Rute Terbaik untuk Distribusi Barang')
    plt.grid()
    plt.show()

# Fungsi untuk menghitung biaya bahan bakar berdasarkan jarak
def calculate_fuel_cost(distance, fuel_price_per_liter, fuel_efficiency):
    return (distance / fuel_efficiency) * fuel_price_per_liter

# Data jarak antar kota di sekitar Bandung berdasarkan Google Map (distance matrix)
distance_matrix = [
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
