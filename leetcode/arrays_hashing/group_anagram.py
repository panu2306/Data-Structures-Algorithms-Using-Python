from collections import defaultdict

def group_anagrams(strs):
    d = {}
    for s in strs:
        a_sum = 0
        for c in s:
            a_sum += ord(c)
        d[s] = d.get(s, 0) + a_sum
    d = dict(sorted(d.items(), key=lambda x:x[1]))
    l = []
    keys = list(d.keys())
    values = list(d.values())
    for index, value in enumerate(values):
        if(index == 0 or  value != values[index-1]):
            curr_group = [keys[index]]
            l.append(curr_group)
        else:
            curr_group.append(keys[index])
    return l

def group_anagrams_1(strs):
    d = defaultdict(list)
    for s in strs:
        d[tuple(sorted(s))].append(s)
    return list(d.values())

def group_anagrams_2(strs):
    d = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1 
        d[tuple(count)].append(s)
    return list(d.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))
print(group_anagrams_1(strs))
print(group_anagrams_2(strs))
