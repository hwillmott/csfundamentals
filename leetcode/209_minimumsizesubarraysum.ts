function minSubArrayLen(target: number, nums: number[]): number {
    let l = 0
    let r = 1
    let currSum = nums[0]
    let shortest = 0

    while (r <= nums.length && l < r) {
        if (currSum >= target) {
            const currLength = r - l
            if (shortest === 0) {
                shortest = currLength
            } else if (shortest > currLength) {
                shortest = currLength
            }
        }

        if (currSum > target) {
            currSum -= nums[l]
            l = l + 1
        } else {
            currSum += nums[r]
            r = r + 1
        }
    }

    return shortest
};
