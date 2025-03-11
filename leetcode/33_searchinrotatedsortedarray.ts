function search(nums: number[], target: number): number {
    let r = nums.length - 1
    let l = 0

    while (l < r) {
        const m = Math.floor((l + r)/2)
        // console.log({l, m, r})
        if (nums[m] === target) return m
        if (nums[l] <= nums[m]) { // left half is sorted
            if (nums[m] > target && nums[l] <= target) { // target in left half
                r = m - 1 // go left
            } else {
                l = m + 1 // go right
            }
        } else { // right half is sorted
            if (nums[m] < target && nums[r] >= target) { // target in right half
                l = m + 1
            } else {
                r = m - 1
            }
        }
    }
    // console.log('final', {l, r})
    if (nums[l] === target) return l
    return -1
};
