class Solution {
    public int[][] sortMatrix(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;

        // process diagonals starting from first row (r = 0, c = col-1..0) -> ascending
        for (int c = col - 1; c > 0; c--) {
            List<Integer> collect = new ArrayList<>();
            int r = 0;
            int tc = c;

            while (r < row && tc < col) {
                collect.add(grid[r][tc]);
                r++;
                tc++;
            }

            // sort ascending
            Collections.sort(collect);

            r = 0;
            tc = c;
            int idx = 0;
            while (r < row && tc < col) {
                grid[r][tc] = collect.get(idx);
                r++;
                tc++;
                idx++;
            }
        }

        // process diagonals starting from first column (c = 0, r = 1..row-1) -> descending
        for (int r = 0; r < row; r++) {
            List<Integer> collect = new ArrayList<>();
            int rc = r;
            int c = 0;

            while (rc < row && c < col) {
                collect.add(grid[rc][c]);
                rc++;
                c++;
            }

            // sort descending
            collect.sort(Collections.reverseOrder());

            rc = r;
            c = 0;
            int idx = 0;
            while (rc < row && c < col) {
                grid[rc][c] = collect.get(idx);
                rc++;
                c++;
                idx++;
            }
        }

        return grid;
    }
}
