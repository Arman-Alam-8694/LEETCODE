class Solution {
    private char[][] board;
    private HashSet<Character>[] rows;
    private HashSet<Character>[] cols;
    private HashSet<Character>[] boxes;

    public void solveSudoku(char[][] board) {
        this.board = board;
        this.rows = new HashSet[9];
        this.cols = new HashSet[9];
        this.boxes = new HashSet[9];

        // Initialize sets
        for (int i = 0; i < 9; i++) {
            rows[i] = new HashSet<>();
            cols[i] = new HashSet<>();
            boxes[i] = new HashSet<>();
        }

        // Populate sets and count remaining cells
        int remain = 0;
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c != '.') {
                    rows[i].add(c);
                    cols[j].add(c);
                    boxes[(i / 3) * 3 + j / 3].add(c);
                } else {
                    remain++;
                }
            }
        }
        
        // Start the recursive solving process from position (0, 0)
        // with the total number of remaining empty cells.
        solve(0, 0, remain);
    }

    /**
     * Attempts to solve the Sudoku puzzle recursively.
     * @param r The current row index to start searching from.
     * @param c The current column index to start searching from.
     * @param remain The number of remaining empty cells.
     * @return true if a solution is found, false otherwise.
     */
    private boolean solve(int r, int c, int remain) {
        // Base case: If there are no more empty cells, we've solved the puzzle.
        if (remain == 0) {
            return true;
        }

        // Find the next empty cell to fill, starting from (r, c)
        int nextRow = r;
        int nextCol = c;
        while (board[nextRow][nextCol] != '.') {
            nextCol++;
            if (nextCol == 9) {
                nextRow++;
                nextCol = 0;
            }
            // If we've reached the end of the board without finding an empty cell,
            // but 'remain' is > 0, something is wrong. This check prevents an infinite loop.
            if (nextRow == 9) {
                return false;
            }
        }

        // Now, at position (nextRow, nextCol), try numbers '1' through '9'
        for (char num = '1'; num <= '9'; num++) {
            if (isValid(nextRow, nextCol, num)) {
                // Place the number
                board[nextRow][nextCol] = num;
                rows[nextRow].add(num);
                cols[nextCol].add(num);
                boxes[(nextRow / 3) * 3 + nextCol / 3].add(num);

                // Recurse: Start the next search from the current position.
                // The `remain` count is decremented.
                if (solve(nextRow, nextCol, remain - 1)) {
                    return true; // A solution was found
                }

                // Backtrack: If the recursive call failed, undo our move
                board[nextRow][nextCol] = '.';
                rows[nextRow].remove(num);
                cols[nextCol].remove(num);
                boxes[(nextRow / 3) * 3 + nextCol / 3].remove(num);
            }
        }
        
        return false; // No number worked for this cell, so we must backtrack further
    }

    /**
     * Checks if a character is valid at the given coordinates.
     */
    private boolean isValid(int row, int col, char c) {
        int boxIndex = (row / 3) * 3 + (col / 3);
        return !rows[row].contains(c) &&
               !cols[col].contains(c) &&
               !boxes[boxIndex].contains(c);
    }
}