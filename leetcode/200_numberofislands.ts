function sink(grid: string[][], i, j) {
    if (0 <= i && i < grid.length && 0 <= j && j < grid[i].length && grid[i][j] === "1") {
        grid[i][j] = "0"
        sink(grid, i+1, j)
        sink(grid, i, j+1)
        sink(grid, i-1, j)
        sink(grid, i, j-1)
        return 1
    }
    return 0
}

function numIslands(grid: string[][]): number {
    let totalIslands = 0
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            totalIslands += sink(grid, i , j)
        }
    }
    return totalIslands
};

function numIslands(grid: string[][]): number {
    let num = 0
    for (let row = 0; row < grid.length; row++) {
        for (let col = 0; col < grid[0].length; col++) {
            if (grid[row][col] === '1') {
                num += 1
                let q = [[row, col]] 
                while (q.length > 0) {
                    const coords = q.shift()
                    const x = coords[0] 
                    const y = coords[1]
                    if (x >= 0 && x < grid.length && y >= 0 && y < grid[0].length && grid[x][y] === '1') {
                        grid[x][y] = '0'
                        q.push([x+1, y])
                        q.push([x, y+1])
                        q.push([x-1,y])
                        q.push([x, y-1])
                    }
                }
            }
        }
    }
    return num
};
