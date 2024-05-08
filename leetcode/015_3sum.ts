function threeSum(nums: number[]): number[][] {
    if (nums.length < 3) return []
    nums.sort((a, b) => {
       return a < b ? -1 : 1
    })
    const result = []
    let i = 0
    while (i < nums.length - 2) {
        if (nums[i] > 0) break
        if (i === 0 || nums[i] !== nums[i-1]) {
            let j = i+1
            let k = nums.length - 1
            while (j < k) {
                const sum = nums[i] + nums[j] + nums[k]
                if (sum === 0) {
                    result.push([nums[i], nums[j], nums[k]])
                    while (j < k && nums[j] === nums[j+1]) { // skip duplicates
                        j += 1
                    }
                    while (j < k && nums[k] === nums[k-1]) { // skip duplicates
                        k -=1
                    }
                    j += 1
                    k -= 1
                } else if (sum < 0) {
                    j += 1
                } else { // sum > 0
                    k -= 1
                }
            }
        }
        i += 1
    }
    return result
};
