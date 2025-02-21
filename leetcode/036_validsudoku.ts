function isValidSudoku(board: string[][]): boolean {
    // validate rows & columns
    for (let i = 0; i < 9; i++) {
        const countsRows = [0,0,0,0,0,0,0,0,0,0]
        const countsColumns = [0,0,0,0,0,0,0,0,0,0]
        for (let j = 0; j < 9; j++) {

            // check i,j
            let currSquare = parseInt(board[i][j])
            if (!isNaN(currSquare) && countsRows[currSquare] > 0) {
                return false
            }
            countsRows[currSquare] = 1

            // check j,i
            currSquare = parseInt(board[j][i])
            if (!isNaN(currSquare) && countsColumns[currSquare] > 0) {
                return false
            }
            countsColumns[currSquare] = 1
        }

    }

    // validate boxes
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            // now we have a "box" in a 3x3 array
            const countsBox = [0,0,0,0,0,0,0,0,0,0]
            const topLeftI = i*3
            const topLeftJ = j*3

            // iterate through the box
            for (let k = 0; k < 3; k++) {
                for (let l = 0; l < 3; l++) {
                    const currSquare = parseInt(board[topLeftI + k][topLeftJ + l])
                    if (!isNaN(currSquare) && countsBox[currSquare] > 0) {
                        return false
                    }
                    countsBox[currSquare] = 1
                }
            }

        }
    }
    return true
};
