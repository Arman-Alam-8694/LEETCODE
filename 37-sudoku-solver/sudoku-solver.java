class Solution {
    private char[][] board;
    private List<HashSet<Character>> rows;
    private List<HashSet<Character>> cols;
    private List<HashSet<Character>> boxes;

    public void solveSudoku(char[][] board) {
        this.board = board;
        this.rows = new ArrayList<>();
        this.cols = new ArrayList<>();
        this.boxes = new ArrayList<>();

        for (int i = 0; i < 9; i++) {
            rows.add(new HashSet<>());
            cols.add(new HashSet<>());
            boxes.add(new HashSet<>());
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c != '.') {
                    rows.get(i).add(c);
                    cols.get(j).add(c);
                    boxes.get((i / 3) * 3 + j / 3).add(c);
                }
            }
        }
        
        solve();
    }

    private boolean solve() {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    for (char c = '1'; c <= '9'; c++) {
                        if (isValid(i, j, c)) {
                            board[i][j] = c;
                            rows.get(i).add(c);
                            cols.get(j).add(c);
                            boxes.get((i / 3) * 3 + j / 3).add(c);

                            if (solve()) {
                                return true;
                            } else {
                                // Backtrack
                                board[i][j] = '.';
                                rows.get(i).remove(c);
                                cols.get(j).remove(c);
                                boxes.get((i / 3) * 3 + j / 3).remove(c);
                            }
                        }
                    }
                    return false; // No number from 1-9 worked for this cell
                }
            }
        }
        return true; // All cells are filled
    }

    private boolean isValid(int row, int col, char c) {
        // Check row, column, and 3x3 box
        return !rows.get(row).contains(c) &&
               !cols.get(col).contains(c) &&
               !boxes.get((row / 3) * 3 + col / 3).contains(c);
    }
}