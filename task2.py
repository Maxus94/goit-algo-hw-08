import heapq

def merge_k_lists(lists):
    list = []
    if len(lists) > 0:
        list = lists[0]
        heapq.heapify(list)        
        for i in range(1, len(lists)):
            for item in lists[i]:
                heapq.heappush(list, item)
    return [heapq.heappop(list) for _ in range(len(list))]

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)