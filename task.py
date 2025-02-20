import heapq

cabels = [1, 1, 2, 3]
heapq.heapify(cabels)
print(cabels) 
connected_cabels = []
sum_cumulative = 0
previous_cable = 0
current_cable = 0

for i in range(0, len(cabels)):
    previous_cable = current_cable + previous_cable
    current_cable = heapq.heappop(cabels)
    sum_current = previous_cable + current_cable
    connected_cabels.append(current_cable)    
    if i > 0:
        sum_cumulative += sum_current                


connected = ''
for cabel in connected_cabels:   
    connected += str(cabel) + " + "

print(connected[:-2:])
print(sum_cumulative)        