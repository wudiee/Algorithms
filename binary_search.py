def binary_search(arr,target,low=None, high = None):
  low,high = low or 0, high or len(arr)-1

  mid = (low+high)//2
  if low>high:
    return -1
  if(arr[mid] > target):
    return binary_search(arr,target,low,mid)
  if(arr[mid]<target):
    return binary_search(arr,target,mid+1,high)
  if arr[mid] == target:
    return mid
    
arr = [1,3,7,8,11,12,15,17,20,25,27,38,41,45,48,50,52,55,57,60,64,68,70,72,74,76,78,81,83,97]

target = 3

print(binary_search(arr,target,low=None,high = None)+1)
