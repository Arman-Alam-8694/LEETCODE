import java.util.*;

class Spreadsheet {
    List<int[]> sheet = new ArrayList<>();

    public Spreadsheet(int rows) {
        for (int i = 0; i < rows; i++) {
            int[] r = new int[26];
            sheet.add(r);
        }
    }

    public void setCell(String cell, int value) {
        char col = cell.charAt(0);
        char temp = 'A';
        String rr = "";
        for (int k = 1; k < cell.length(); k++) {
            rr += cell.charAt(k);
        }
        int realCol = (int) col - (int) temp;
        int realRow = Integer.valueOf(rr);
        sheet.get(realRow - 1)[realCol] = value;
    }

    public void resetCell(String cell) {
        char col = cell.charAt(0);
        char temp = 'A';
        String rr = "";
        for (int k = 1; k < cell.length(); k++) {
            rr += cell.charAt(k);
        }
        int realCol = (int) col - (int) temp;
        int realRow = Integer.valueOf(rr);
        sheet.get(realRow - 1)[realCol] = 0;
    }

    public int getValue(String formula) {
        // Remove '=' at the start if present
        if (formula.charAt(0) == '=') {
            formula = formula.substring(1);
        }

        String[] parts = formula.split("\\+");
        int result = 0;
        for (String part : parts) {
            part = part.trim();
            if (Character.isLetter(part.charAt(0))) {
                // It's a cell reference
                char col = part.charAt(0);
                char temp = 'A';
                String rr = "";
                for (int k = 1; k < part.length(); k++) {
                    rr += part.charAt(k);
                }
                int realCol = (int) col - (int) temp;
                int realRow = Integer.valueOf(rr);
                result += sheet.get(realRow - 1)[realCol];
            } else {
                // It's a number
                result += Integer.valueOf(part);
            }
        }
        return result;
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet obj = new Spreadsheet(rows);
 * obj.setCell(cell,value);
 * obj.resetCell(cell);
 * int param_3 = obj.getValue(formula);
 */
