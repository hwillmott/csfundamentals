function findMin(nums: number[]): number {
  let l = 0
  let r = nums.length - 1

  while (l < r) {
    const mid = Math.floor((r + l) / 2)
    if (nums[mid] > nums[r]) { // min is on the right side
      l = mid + 1
    } else {
      r = mid
    }
  }
  
  return nums[r]
}; 
