def find_min(a):
        # METHOD 1:
        #for i in range(len(a)):
        #       if(i+1 < len(a)):
        #               if(a[i] < a[i+1]):
        #                       temp = a[i+1]
        #                       a[i+1] = a[i]
        #                       a[i] = temp

        #return a[-1]

        # METHOD 2:
        #for i in range(len(a)):
        #       min = a[0]
        #       if(min > a[i]):
        #               min = a[i]

        #return min

        # METHOD 3(Pythonic Way:BOSS):
        return min(a)

def find_min_index(a):
        for i in range(len(a)):
                min_index = 0
                if(a[min_index] > a[i]):
                        min_index = i

        return min_index

a = [54, 5, 33, 2, 6, 9, 1]

print("Index of  Minimum Valued Element:", find_min_index(a))
print("Minimum Valued Element:", find_min(a))
