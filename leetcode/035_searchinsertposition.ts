function searchInsert(nums: number[], target: number): number {
    if (nums.length === 0) return 0
    if (nums.length === 1) return nums[0] >= target ? 0 : 1
    let left = 0
    let right = nums.length - 1
    while (left < right) {
        const mid = Math.round((right + left)/2)

        if (nums[mid] === target) return mid
        if (nums[mid] < target) {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    if (nums[left] < target) {
        return left + 1
    } 
    return left
};

function searchInsert(nums: number[], target: number): number {
    let l = 0
    let r = nums.length - 1
    while (l < r) {
        const m = Math.floor((r-l)/2 + l)
        console.log({l, m, r, num: nums[m]})
        if (nums[m] > target) {
            r = m - 1
        } else if (nums[m] === target) {
            return m
        } else {
            l = m + 1
        }
    }
    return nums[l] < target ? l + 1 : l
};
