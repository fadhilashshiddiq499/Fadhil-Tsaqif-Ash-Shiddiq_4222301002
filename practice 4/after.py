import numpy as np
import matplotlib.pyplot as plt

# DATA
X = np.array([
    [1,1],[2,1],[3,2],[4,2],
    [5,3],[6,3],[7,4],[8,4],
    [9,5],[10,5]
])

y = np.array(['A','A','A','A','B','B','B','B','A','A'])

# Titik baru
new_point = np.array([6,5])

# Hitung jarak Euclidean
distances = np.sqrt(np.sum((X - new_point)**2, axis=1))

# Urutkan
sorted_idx = np.argsort(distances)

# Ambil K = 5
k = 5
neighbors_idx = sorted_idx[:k]

# =========================
# VISUALISASI BEFORE
# =========================
plt.figure()

for i in range(len(X)):
    if y[i] == 'A':
        plt.scatter(X[i][0], X[i][1], marker='o')
    else:
        plt.scatter(X[i][0], X[i][1], marker='x')

# Titik baru
plt.scatter(new_point[0], new_point[1], marker='*', s=200)

plt.title("BEFORE (Data Awal)")
plt.xlabel("X1")
plt.ylabel("X2")

# =========================
# VISUALISASI AFTER
# =========================
plt.figure()

for i in range(len(X)):
    if y[i] == 'A':
        plt.scatter(X[i][0], X[i][1], marker='o')
    else:
        plt.scatter(X[i][0], X[i][1], marker='x')

# Highlight tetangga terdekat
for i in neighbors_idx:
    plt.scatter(X[i][0], X[i][1], s=200, facecolors='none', edgecolors='black')

# Titik baru
plt.scatter(new_point[0], new_point[1], marker='*', s=200)

plt.title("AFTER (KNN, K=5)")
plt.xlabel("X1")
plt.ylabel("X2")

plt.show()