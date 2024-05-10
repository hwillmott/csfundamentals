function isSubsequence(s: string, t: string): boolean {
  let sP = 0
  let tP = 0

  while (sP < s.length && tP < t.length) {
    if (s[sP] === t[tP]) {
      sP += 1
    }
    tP += 1
  }

  if (sP === s.length) return true
    
  return false
};
