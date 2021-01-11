def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in array:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
def match(arr,selected):
  cnt = 0
  for i in arr:
    for j in selected:
      if i==j:
        cnt+=1
  return cnt

if __name__ == "__main__":
  arr = [485,241,454,325,452,685,498,890,281,121]
  selected = [486,242,454,325,453,685,499,891,282,122]
  arr = quick_sort(arr)
  selected = quick_sort(selected)
  cnt = match(arr,selected)
  print(arr)
  print(selected)
  print(cnt)