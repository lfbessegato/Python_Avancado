# heapq -> implementa filas de prioridades
import heapq
idades = [15, 10, 20, 18, 25, 8, 19]
print(idades)

# 3 menores idades
print(heapq.nsmallest(3, idades))

# 4 maiores elementos
print(heapq.nlargest(4, idades))

# heapq.heappop -> remove da menor posição
# heapq.heappush -> insere na menor posição