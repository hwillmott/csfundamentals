function maxArea(height: number[]): number {
  // start with the widest container possible
  let currLeft = 0
  let currRight = height.length
  let maxLeft = currLeft
  let maxRight = currRight
  let maxVolume = 0
  while (currLeft < currRight) {
    const currVolume = (currRight - currLeft) * Math.min(height[currLeft], height[currRight])
    if (currVolume > maxVolume) {
      maxVolume = currVolume
      maxLeft = currLeft
      maxRight = currRight
    }

    if (height[currLeft] < height[currRight]) {
      currLeft += 1
    } else {
      currRight -= 1
    }
  }

    return maxVolume
};

function maxArea(height: number[]): number {
    let left = 0
    let right = height.length - 1
    let maxV = 0

    while (left < right) {
        let v = Math.min(height[left], height[right]) * (right - left)
        maxV = Math.max(v, maxV)
        if (height[left] < height[right]) {
            left = left + 1
        } else {
            right = right - 1
        }
    }

    return maxV
};
