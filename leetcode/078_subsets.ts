function subsets(nums: number[]): number[][] {
    const res = []
    generate(nums, [], 0, res)
    return res
};

function generate(nums: number[], currSet: number[], idx: number, result: number[][]) {
    result.push(currSet)
    if (idx >= nums.length) {
        return
    }
    for (let i = idx; i < nums.length; i++) {
        generate(nums, [...currSet, nums[i]], i+1, result)
    }  
}
