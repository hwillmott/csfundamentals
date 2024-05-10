function longestCommonPrefix(strs: string[]): string {
    strs.sort()
    const firstWord = strs[0]
    const lastWord = strs[strs.length - 1]
    const maxLen = Math.min(firstWord.length, lastWord.length)
    let idx = 0
    for (let i = 0; i < maxLen; i++) {
        if (firstWord[i] !== lastWord[i]) break
        idx += 1
    }

    return firstWord.substring(0, idx)
};
