
def linearSearch(arr, key):
    for i in arr:
        if i==key:
            return arr.index(i)
    return "Key not Found"

print("Enter the elements of the list(space seperated)")
arr = list(map(int,input().strip().split()))
key = int(input("Enter Key to search: "))
result = linearSearch(arr,key)
print(result)