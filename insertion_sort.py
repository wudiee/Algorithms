def insertion_sort(arr,num):
    for end in range(1, len(arr)):
        i = end
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
    print(arr)
    for i in range(len(arr)):
      if arr[i] == num:
        return i+1
if __name__ == "__main__":
  arr = [35,9,8,18,98,31,58,17,76,45]
  num = 31
  print(insertion_sort(arr,num))