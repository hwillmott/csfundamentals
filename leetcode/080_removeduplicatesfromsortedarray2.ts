function removeDuplicates(nums: number[]): number {
    let readIdx = 2
    let writeIdx = 2
    while (readIdx < nums.length) {
        if (nums[readIdx] !== nums[writeIdx-2]) {
            nums[writeIdx] = nums[readIdx]
            writeIdx += 1
        } 
        readIdx += 1
    }
    return writeIdx
};
