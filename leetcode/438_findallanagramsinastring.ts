function findAnagrams(s: string, p: string): number[] {
    const pSorted = p.split('').sort()
    const pLen = p.length
    const indices: number[] = []
    const sChars = s.split('')
    for (let i = 0; i <= s.length-pLen; i++) {
        let isSame = true
        const subSorted = sChars.slice(i, i+pLen).sort()
        for (let j = 0; j < pLen; j++) {
            if (subSorted[j] !== pSorted[j]) {
                isSame = false
            }
        }
        if (isSame) {
            indices.push(i)
        }
    }
    return indices
};
// time limit exceeded
