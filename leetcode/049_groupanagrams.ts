function groupAnagrams(strs: string[]): string[][] {
    const dict: {[id: string]: string[]} = {}
    strs.forEach((s: string) => {
        const inOrder = s.split('').sort().join('')
        if (dict[inOrder]) {
            dict[inOrder].push(s)
        } else {
            dict[inOrder] = [s]
        }
    })
    return Object.values(dict)
};
