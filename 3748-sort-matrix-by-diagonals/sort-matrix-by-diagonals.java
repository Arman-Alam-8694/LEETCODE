import java.util.*;

class Solution {
    public int[][] sortMatrix(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;

        // Top-right diagonals (row = 0, c = col-1..0) → ascending
        for (int c = col - 1; c > 0; c--) {
            processDiagonal(grid, 0, c, true); // ascending
        }

        // Bottom-left diagonals (col = 0, r = 1..row-1) → descending
        for (int r = 0; r < row; r++) {
            processDiagonal(grid, r, 0, false); // descending
        }

        return grid;
    }

    // Helper to collect, sort, and write back a diagonal
    private void processDiagonal(int[][] grid, int r, int c, boolean ascending) {
        int row = grid.length;
        int col = grid[0].length;

        List<Integer> collect = new ArrayList<>();

        // Collect diagonal
        int i = r, j = c;
        while (i < row && j < col) {
            collect.add(grid[i][j]);
            i++;
            j++;
        }

        // Sort based on order
        if (ascending) {
            Collections.sort(collect);
        } else {
            collect.sort(Collections.reverseOrder());
        }

        // Write back
        i = r;
        j = c;
        int idx = 0;
        while (i < row && j < col) {
            grid[i][j] = collect.get(idx++);
            i++;
            j++;
        }
    }
}
