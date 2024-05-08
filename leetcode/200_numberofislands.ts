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
