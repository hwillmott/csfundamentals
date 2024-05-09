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
