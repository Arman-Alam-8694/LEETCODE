import java.util.*;

class Spreadsheet {

    Map<String, Integer> map = new HashMap<>();

    public Spreadsheet(int rows) {
        // rows are not used in HashMap approach, but we keep the constructor
    }

    public void setCell(String cell, int value) {
        map.put(cell, value);
    }

    public void resetCell(String cell) {
        map.remove(cell);
    }

    public int getValue(String formula) {
        // Expect formula like "=A1+5" or "=10+B2"
        int io = formula.indexOf('+');

        // First operand (skip '=' at start)
        StringBuilder sb1 = new StringBuilder();
        for (int i = 1; i < io; i++) {
            sb1.append(formula.charAt(i));
        }
        String cell1 = sb1.toString();

        // Second operand
        StringBuilder sb2 = new StringBuilder();
        for (int i = io + 1; i < formula.length(); i++) {
            sb2.append(formula.charAt(i));
        }
        String cell2 = sb2.toString();

        int val1;
        if (Character.isLetter(cell1.charAt(0))) { // Cell reference
            val1 = map.getOrDefault(cell1, 0);
        } else { // Integer literal
            val1 = Integer.parseInt(cell1);
        }

        int val2;
        if (Character.isLetter(cell2.charAt(0))) {
            val2 = map.getOrDefault(cell2, 0);
        } else {
            val2 = Integer.parseInt(cell2);
        }

        return val1 + val2;
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet obj = new Spreadsheet(rows);
 * obj.setCell(cell,value);
 * obj.resetCell(cell);
 * int param_3 = obj.getValue(formula);
 */
