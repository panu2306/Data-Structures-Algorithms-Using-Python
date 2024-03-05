def find_intersected_elements(set1, set2):
    return [x for x in set1 if x in set2]

def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    if(len(set1) < len(set2)):
        return find_intersected_elements(set1, set2)
    else:
        return find_intersected_elements(set2, set1)

nums1 = [4,9,5]
nums2 = [9,4, 9, 8, 4]

print(intersection(nums1, nums2))
