function removeDuplicates(nums: number[]): number {
    let writeIdx = 1
    let readIdx = 1
    
    while (readIdx < nums.length) {
        if (nums[readIdx] === nums[writeIdx - 1]){
            readIdx = readIdx + 1
            continue
        } 

        nums[writeIdx] = nums[readIdx]
        writeIdx = writeIdx + 1
        readIdx = readIdx + 1
    }

    return writeIdx
};
