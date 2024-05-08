function findRepeatedDnaSequences(s: string): string[] {
    const allSubstrings: {[key: string]: number} = {}
    for (let start = 0; start <= s.length-10; start++) {
        let end = start + 10
        const sub = (end >= s.length) ? s.substring(start) : s.substring(start, end)
        if (allSubstrings[sub]) {
            allSubstrings[sub] += 1
        } else {
            allSubstrings[sub] = 1
        }
    }

    const results: string[] = []

    Object.entries(allSubstrings).map(([key, value]) => {
        if (value > 1) {
            results.push(key)
        }
    })
    return results
};
