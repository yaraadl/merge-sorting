#yara adel hassan mohamed 19100683 algorithm year work project
def mergeSort(arr):
    if len(arr) > 1:
        r = len(arr)//2
        L = arr[:r]
        M = arr[r:]
        mergeSort(L)
        mergeSort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            arr[k] = M[j]
            j += 1
            k += 1
def print(arr):
    for i in range(len(arr)):
        print(arr[i])
    print()
if __name__ == '__main__':
    arr = [9, 1, 3, 2, 7, 4]
    print("un Sorted array : ")
    print(arr)
    mergeSort(arr)
    print("Sorted array : ")
    print(arr)