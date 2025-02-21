/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
    const numRows = matrix.length
    const numCols = matrix[0].length
    const rowsToSet = {}
    const colsToSet = {}

    for (let i = 0; i < numRows; i++) {
        for (let j = 0; j < numCols; j++) {
            if (matrix[i][j] === 0) {
                rowsToSet[i] = 1
                colsToSet[j] = 1
            }
        }
    }

    const rows = Object.keys(rowsToSet)
    rows.forEach((row) => {
        for (let c = 0; c < numCols; c++) {
            matrix[row][c] = 0
        }
    })
    const columns = Object.keys(colsToSet)
    columns.forEach((col) => {
        for (let r = 0; r < numRows; r++) {
            matrix[r][col] = 0
        }
    })
};
