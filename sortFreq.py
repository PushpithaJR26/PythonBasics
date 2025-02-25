#sort by frequency: sort elements by their frequency, with the msot frequent elements first.
#input:[1,1,2,2,2,3]
#output:[2,2,2,1,1,3]

def sort_by_frequency(arr):
    return sorted(arr,key=lambda x: (-arr.count(x), x))

arr = [1,1,2,2,2,3]
print(sort_by_frequency(arr))
