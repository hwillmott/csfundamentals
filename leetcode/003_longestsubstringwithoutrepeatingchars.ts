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
