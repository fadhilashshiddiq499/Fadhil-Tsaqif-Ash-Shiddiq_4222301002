import numpy as np
import matplotlib.pyplot as plt

# Data (contoh, sesuaikan dengan tabel kamu)
X = np.array([
    [1,1],[2,1],[3,2],[4,2],
    [5,3],[6,3],[7,4],[8,4],
    [9,5],[10,5]
])

y = ['A','A','A','A','B','B','B','B','A','A']

# Titik baru
new_point = np.array([6,5])

# Hitung jarak
distances = np.sqrt(np.sum((X - new_point)**2, axis=1))

# Gabungkan & urutkan
data = list(zip(X, y, distances))
data_sorted = sorted(data, key=lambda x: x[2])

# Ambil K=5
k = 5
neighbors = data_sorted[:k]

# Voting
labels = [n[1] for n in neighbors]
prediksi = max(set(labels), key=labels.count)

print("Tetangga terdekat:", neighbors)
print("Hasil KNN:", prediksi)

# Visualisasi
for i in range(len(X)):
    if y[i] == 'A':
        plt.scatter(X[i][0], X[i][1])
    else:
        plt.scatter(X[i][0], X[i][1])

plt.scatter(new_point[0], new_point[1], marker='x', s=100)
plt.title("Visualisasi KNN")
plt.show()