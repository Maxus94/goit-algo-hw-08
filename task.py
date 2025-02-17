import heapq

cabels = [4, 10, 3, 5, 1, 1, 2, 2, 2, 1, 3, 7]
heapq.heapify(cabels)
print(cabels) 
connected_cabels = []

for _ in range(0, len(cabels)):
    connected_cabels.append(heapq.heappop(cabels))

connected = ''
for cabel in connected_cabels:   
    connected += str(cabel) + " + "

print(connected[:-2:])