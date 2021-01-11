def selection_sort(arr,arr2):

  for i in range(len(arr) - 1):
      min_idx = i
      for j in range(i + 1, len(arr)):
          if arr[j] < arr[min_idx]:
              min_idx = j
      arr[i], arr[min_idx] = arr[min_idx], arr[i]
  res = []
  res.append([arr[0],"F"])
  res.append([arr[1],"D"])
  res.append([arr[2],"D+"])
  res.append([arr[3],"C"])
  res.append([arr[4],"C+"])
  res.append([arr[5],"B"])
  res.append([arr[6],"B+"])
  res.append([arr[7],"A"])
  res.append([arr[8],"A+"])
  res.append([arr[9],"A+"])

  answer = []

  for i in arr2:
    for j in range(len(res)):
      if i == res[j][0]:
        answer.append(res[j][1])

  return answer

if __name__ == "__main__":
  arr = [41,31,48,97,9,65,27,29,13,15]
  arr2 = [41,31,48,97,9,65,27,29,13,15]
  print(selection_sort(arr,arr2))