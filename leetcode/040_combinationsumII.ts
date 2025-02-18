function combinationSum2(candidates: number[], target: number): number[][] {
    if (candidates.length === 0) return []
    candidates.sort()
    const res = []
    generate(candidates, target, 0, [], 0, res)
    return res
};

function generate(candidates: number[], target: number, currSum: number, currList: number[], idx: number, results: number[][]) {
    if (currSum > target) return
    if (currSum === target) {
        results.push(currList)
        return
    }

    for (let i = idx; i < candidates.length; i++) {
        if (i > idx && candidates[i] === candidates[i-1]) continue
        generate(candidates, target, currSum + candidates[i], [...currList, candidates[i]], i + 1, results)
    }
}
