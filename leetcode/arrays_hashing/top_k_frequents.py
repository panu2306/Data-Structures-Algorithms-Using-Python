# Naive Approach: O(nlogn)
def topKFrequent(nums, k):
    hashmap = {}
    for num in nums:
        hashmap[num] = hashmap.get(num, 0) + 1
    hashmap = dict(sorted(hashmap.items(), key=lambda x:x[1], reverse=True))
    l = []
    for i in range(k):
        l.append(list(hashmap.keys())[i])
    return l 

# using heap data structure: 
def topKFrequent_1(nums, k):
    pass



nums = [1, 1, 1, 2, 2, 3]
k = 2 
print(topKFrequent(nums, k))
