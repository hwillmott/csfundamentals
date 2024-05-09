function majorityElement(nums: number[]): number {
  nums.sort((a, b) => {
      return a < b ? -1 : 1
  })

  const threshold = Math.floor(nums.length / 2) + 1
  let currNum = nums[0]
  let currCount = 1
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] === nums[i-1]) {
      currCount += 1
      if (currCount === threshold) {
        return currNum
      }
    } else {
      currCount = 1
      currNum = nums[i]
    }
  }

  return currNum
};
