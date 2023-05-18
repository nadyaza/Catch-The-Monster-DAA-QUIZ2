import heapq

def shortest_path(graph, start, end, route):
    distances = {}  # menyimpan jarak terpendek dari titik awal ke setiap titik
    previous_nodes = {}  # menyimpan titik sebelumnya yang terhubung dengan setiap titik
    heap = []  # heap untuk mengurutkan titik berdasarkan jarak

    # Menginisialisasi jarak semua titik dengan nilai tak terbatas, kecuali titik awal yang bernilai 0
    for vertex in graph:
        distances[vertex] = float('inf')
    distances[start] = 0

    # Menambahkan titik awal ke dalam heap
    heapq.heappush(heap, (distances[start], start))

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        # Jika jarak terpendek saat ini lebih besar dari jarak yang sudah ada, lewati titik ini
        if current_distance > distances[current_node]:
            continue

        # Jika sudah mencapai titik akhir, hentikan algoritma
        if current_node == end:
            break

        # Iterasi melalui tetangga-tetangga titik saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika jarak baru lebih pendek dari jarak sebelumnya, perbarui nilai jarak dan titik sebelumnya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))

    # Membangun jalur terpendek dari titik awal ke titik akhir
    path = []
    current = end
    while current in previous_nodes:
        path.insert(0, current)
        current = previous_nodes[current]
    path.insert(0, start)

    print(f"Jalur terpendek dari {start} ke {end}: {path}")
    print(f"Jalur dilewati dari {start} ke {end}: {route}")
    if route == path:
        return 2
    else:
        return -1

pos = []    
map = []
Mgraph = {}

def insertPos(index) :
    pos.append(index)
    #print(pos)
    
def draw(sign) :
    map.append(sign)
    #print(map)
    
def roadMap() :
    for element in pos :
        temp = {}
        
        #Search left branch
        i = map.index(element) - 1
        sign = 'l'
        distance_l = 0
        while(i > 0 and i < len(map)) :
            #print(map[i])
            distance_l += 1
            if(map[i] == '1') :
                sign = 'l'
            elif(map[i] == '2') :
                sign = 'u'
            elif(map[i] == '3') :
                sign = 'd'
            elif(map[i] == '4') :
                sign = 'l'
            elif(map[i] == "*") :
                sign = sign
            elif(map[i] == "!") :
                sign = 'f'
            elif(map[i] == '#') :
                sign = 'f'
            else :
                temp[map[i]] = distance_l
                #roadMap(map[i])
                sign = 'f'
        
            if(sign == 'd') : i += 20
            elif(sign == 'u') : i -= 20
            elif(sign == 'l') : i -= 1
            elif(sign == 'f') : i = 0
            
        #Search top branch
        i = map.index(element) - 20
        sign = 'u'
        distance_u = 0
        while(i > 0 and i < len(map)) :
            #print(map[i])
            distance_u += 1
            if(map[i] == '1') :
                sign = 'l'
            elif(map[i] == '2') :
                sign = 'u'
            elif(map[i] == '3') :
                sign = 'r'
            elif(map[i] == '4') :
                sign = 'l'
            elif(map[i] == "*") :
                sign = sign
            elif(map[i] == "!") :
                sign = 'f'
            elif(map[i] == '#') :
                sign = 'f'
            else :
                temp[map[i]] = distance_u
                #roadMap(map[i])
                sign = 'f'
            
            if(sign == 'd') : i += 20
            elif(sign == 'u') : i -= 20
            elif(sign == 'l') : i -= 1
            elif(sign == 'r') : i += 1
            elif(sign == 'f') : i = 0
        
        #Search right branch
        i = map.index(element) + 1
        sign = 'r'
        distance_r = 0
        while(i > 0 and i < len(map)) :
            #print(map[i])
            distance_r += 1
            if(map[i] == '1') :
                sign = 'd'
            elif(map[i] == '2') :
                sign = 'r'
            elif(map[i] == '3') :
                sign = 'r'
            elif(map[i] == '4') :
                sign = 'u'
            elif(map[i] == "*") :
                sign = sign
            elif(map[i] == "!") :
                sign = 'f'
            elif(map[i] == '#') :
                sign = 'f'
            else :
                temp[map[i]] = distance_r
                #roadMap(map[i])
                sign = 'f'
            
            if(sign == 'd') : i += 20
            elif(sign == 'u') : i -= 20
            elif(sign == 'l') : i -= 1
            elif(sign == 'r') : i += 1
            elif(sign == 'f') : i = 0

        #Search bottom branch
        i = map.index(element) + 20
        sign = 'd'
        distance_d = 0
        while(i > 0 and i < len(map)) :
            #print(map[i])
            distance_d += 1
            if(map[i] == '1') :
                sign = 'd'
            elif(map[i] == '2') :
                sign = 'r'
            elif(map[i] == '3') :
                sign = 'd'
            elif(map[i] == '4') :
                sign = 'l'
            elif(map[i] == "*") :
                sign = sign
            elif(map[i] == "!") :
                sign = 'f'
            elif(map[i] == '#') :
                sign = 'f'
            else :
                temp[map[i]] = distance_d
                #roadMap(map[i])
                sign = 'f'
            
            if(sign == 'd') : i += 20
            elif(sign == 'u') : i -= 20
            elif(sign == 'l') : i -= 1
            elif(sign == 'r') : i += 1
            elif(sign == 'f') : i = 0
              
        Mgraph[element] = temp 

def printG() :
    for node, branch in Mgraph.items():
        print(node, branch)
        
def check(Route) :
    win = shortest_path(Mgraph, 'T', 'B', Route)
    return win
