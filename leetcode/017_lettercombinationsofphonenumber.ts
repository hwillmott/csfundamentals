function letterCombinations(digits: string): string[] {
    const res = []
    if (digits.length === 0) return []
    generate(digits, "", res)
    return res  
};

function generate(digits: string, currStr: string, results: string[]) {
    if (digits.length === 0) {
        results.push(currStr)
        return
    }
    const letterMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    const letters = letterMap[digits[0]].split('')
    letters.forEach((ch) => {
        generate(digits.substring(1), currStr + ch, results)
    })
}
