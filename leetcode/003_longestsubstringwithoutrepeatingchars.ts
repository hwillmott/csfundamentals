function lengthOfLongestSubstring(s: string): number {
    let maxLen = 0
    // for each index of the string,
    // iterate over the next chars until a duplicate is found
    const chars = s.split('')
    console.log(chars)
    let currStr = ""

    chars.forEach((ch) => {
        if (currStr.includes(ch)) { // found a dupe char
            // find the index of that char and start the new string from the char that follows
            const firstIdx = currStr.indexOf(ch)
            currStr = currStr.substring(firstIdx + 1) + ch
            console.log("one ", currStr)
        } else { // found a new char
            console.log("two ", currStr)
            currStr = currStr + ch
            if (currStr.length > maxLen) { // update the max
                maxLen = currStr.length
            }
        }
    })

    return maxLen
};

function lengthOfLongestSubstring(s: string): number {
    if (s.length <= 1) return s.length
    let left = 0
    let right = 0
    const counts: {[id: string] : number} = {}
    let longest = 1
    counts[s[0]] = 1

    while (right < s.length - 1) {
        // move right index up
        right = right + 1
        counts[s[right]] = counts[s[right]] ? counts[s[right]] + 1 : 1

        // if duplicates move left index until not true
        while (counts[s[right]] > 1) {
            counts[s[left]] -= 1
            left += 1
        }

        if (right - left + 1 > longest) {
            longest = right - left + 1
        } 
    }
    return longest
};
