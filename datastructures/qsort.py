def qsort(nums, lo, hi):
  if lo < hi:
    p = partition(nums, lo, hi)
    qsort(nums, lo, p-1)
    qsort(nums, p+1, hi)
  
def partition(nums, lo, hi):
  pivot = nums[hi]
  i = lo
  for j in range(lo, hi):
    if nums[j] <= pivot:
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
  nums[i], nums[hi] = nums[hi], nums[i]
  return i
  
def sortQ(nums):
  qsort(nums, 0, len(nums)-1)
  print(nums)
  
sortQ([4,6,9,4,1,2,7,4,9,8,0,1,2,6,3,7])