

def bublesort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-1, -1):
			if arr[j] > arr[j+1]:
				a[j], arr[j+1] = arr[j+1], arr[j]
	return arr

def selectionsort(arr):
	n = len(arr)
	for i in range(n):
		min_idx = i
		for j in range(i+1, n):
			if arr[j] < arr[min_idx]:
				min_idx = j
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
	return arr

def insertionsort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr
