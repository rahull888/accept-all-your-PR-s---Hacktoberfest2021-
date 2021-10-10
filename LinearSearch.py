def linearSearch(arr, findKey):
    for value in arr:
        if findKey == value:
            return f'{findKey} Key is Found at index : {arr.index(value) + 1}'
    return "Key not found"



print(linearSearch([1,2,3,4,5,6], 3))
print(linearSearch([1,2,3,4,5,6], 9))
print(linearSearch([1,2,3,4,5,6], 2))