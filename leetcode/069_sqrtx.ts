function mySqrt(x: number): number {
    if (x < 2) return x
    // binary search from 2-x/2
    let right = Math.floor(x/2)
    let left = 0

    let found = false

    while (!found) {
        const middle = Math.floor((right-left)/2) + left
        const msq = middle * middle
        if (msq > x) { // go down
            right = middle - 1
            continue
        }
        const mplus = (middle+1) * (middle+1)
        if (mplus <= x) { // go up
            left = middle + 1
            continue
        }

        found = true
        return middle
    }
};
