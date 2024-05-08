function addMore(currNums: number[], currSum: number, idx: number, candidates: number[], target: number, results: number[][]) {
    if (currSum > target) return
    if (currSum === target) {
        results.push(currNums)
    }
    for (let i = idx; i < candidates.length; i++) {
        addMore([candidates[i], ...currNums], currSum + candidates[i], i, candidates, target, results)
    }
}

function combinationSum(candidates: number[], target: number): number[][] {
    const allCombos: number[][] = []
    addMore([], 0, 0, candidates, target, allCombos)
    return allCombos
};
