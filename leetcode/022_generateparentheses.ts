function addParenthesis(currStr, currLeft, currRight, max, resultStrings) {
    if (currLeft === max && currRight === max) {
        resultStrings.push(currStr)
        return
    }
    if (currLeft > currRight) {
        addParenthesis(currStr + ")", currLeft, currRight + 1, max, resultStrings)
    }
    if (currLeft < max) {
        addParenthesis(currStr + "(", currLeft + 1, currRight, max, resultStrings)
    }
}

function generateParenthesis(n: number): string[] {
    const resultStrings: string[] = []
    addParenthesis("", 0, 0, n, resultStrings)
    return resultStrings
};
