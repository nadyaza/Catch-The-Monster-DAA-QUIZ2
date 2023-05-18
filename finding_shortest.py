import heapq

def shortest_path(graph, start, finish, path):
    length = {}  # menyimpan jarak terpendek dari titik awal ke setiap titik
    prev = {}  # menyimpan titik sebelumnya yang terhubung dengan setiap titik
    stack = []  # stack untuk mengurutkan titik berdasarkan jarak

    # Menginisialisasi jarak semua titik dengan nilai tak terbatas, kecuali titik awal yang bernilai 0
    for vertex in graph:
        length[vertex] = float('inf')
    length[start] = 0

    # Menambahkan titik awal ke dalam stack
    heapq.heappush(stack, (length[start], start))

    while stack:
        current_distance, current_node = heapq.heappop(stack)

        # Jika jarak terpendek saat ini lebih besar dari jarak yang sudah ada, lewati titik ini
        if current_distance > length[current_node]:
            continue

        # Jika sudah mencapai titik akhir, hentikan algoritma
        if current_node == finish:
            break

        # Iterasi melalui tetangga-tetangga titik saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika jarak baru lebih pendek dari jarak sebelumnya, perbarui nilai jarak dan titik sebelumnya
            if distance < length[neighbor]:
                length[neighbor] = distance
                prev[neighbor] = current_node
                heapq.heappush(stack, (distance, neighbor))

    # Membangun jalur terpendek dari titik awal ke titik akhir
    path = []
    current = finish
    while current in prev:
        path.insert(0, current)
        current = prev[current]
    path.insert(0, start)

    print(f"Jalur terpendek dari {start} ke {finish}: {path}")
    print(f"Jalur dilewati dari {start} ke {finish}: {path}")
    if path == path:
        return 2
    else:
        return -1

Mgraph = {
    'A': {'D': 9, 'C': 2},
    'B': {'E': 10, 'I': 3},
    'C': {'G': 3, 'A': 2, 'F': 4},
    'D': {'A': 9, 'E': 2},
    'E': {'D': 2, 'B': 10},
    'F': {'C': 4, 'K': 6},
    'G': {'C': 3, 'K': 3},
    'H': {'J': 5, 'I': 7, 'P': 8},
    'I': {'H': 7, 'B': 3, 'L': 3},
    'J': {'H': 5, 'N': 4},
    'K': {'G': 3, 'F': 6, 'M': 2},
    'L': {'I': 3, 'X': 14},
    'M': {'K': 2, 'N': 6, 'T': 4},
    'N': {'M': 6, 'J': 4, 'O': 1},
    'O': {'N': 1, 'R': 2},
    'P': {'H': 8, 'Q': 2, 'S': 4},
    'Q': {'P': 2, 'W': 8},
    'R': {'U': 5, 'O': 2, 'S': 4},
    'S': {'R': 4, 'P': 4, 'W': 2},
    'T': {'M': 4, 'U': 4},
    'U': {'T': 4, 'R': 5, 'V': 4},
    'V': {'U': 4, 'W': 3},
    'W': {'V': 3, 'S': 2, 'Q': 8, 'X': 2},
    'X': {'W': 2, 'L': 14}
}

path = ['T', 'M', 'N', 'J', 'H', 'I', 'B']
result = shortest_path(Mgraph, 'T', 'B', path)
print(f"Result: {result}")
