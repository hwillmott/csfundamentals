function lengthOfLastWord(s: string): number {
    let s2 = s.trim()
    const l = s2.length
    let lastSpaceIdx = -1
    for (let i = 0; i < l; i++) {
        if (s2[i] === ' ') {
            lastSpaceIdx = i
        }
    }
    if (lastSpaceIdx === -1) return l
    return l - (lastSpaceIdx + 1)
};

// "Hello World" l = 11, LSI = 5
