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

function findRepeatedDnaSequences(s: string): string[] {
    const counts: {[id: string]: number} = {}
    if (s.length < 10) return []
    let l = 0
    let r = 9
    while (r < s.length) {
        const sub = s.substring(l, r+1)
        counts[sub] = counts[sub] ? counts[sub] + 1 : 1
        l = l + 1
        r = r + 1
    }

    const results = []
    for (const [key, value] of Object.entries(counts)) {
        if (value > 1) results.push(key)
    } 
    return results
};
