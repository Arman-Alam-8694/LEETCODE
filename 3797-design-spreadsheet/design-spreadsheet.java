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
        
        StringBuilder sb = new StringBuilder();
        for (int k = 1; k < cell.length(); k++) {
            sb.append(cell.charAt(k));
        }
        int realCol = col - temp;
        int realRow = Integer.parseInt(sb.toString());
        
        sheet.get(realRow - 1)[realCol] = value;
    }

    public void resetCell(String cell) {
        char col = cell.charAt(0);
        char temp = 'A';
        
        StringBuilder sb = new StringBuilder();
        for (int k = 1; k < cell.length(); k++) {
            sb.append(cell.charAt(k));
        }
        int realCol = col - temp;
        int realRow = Integer.parseInt(sb.toString());
        
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

                StringBuilder sb = new StringBuilder();
                for (int k = 1; k < part.length(); k++) {
                    sb.append(part.charAt(k));
                }
                int realCol = col - temp;
                int realRow = Integer.parseInt(sb.toString());
                
                result += sheet.get(realRow - 1)[realCol];
            } else {
                // It's a number
                result += Integer.parseInt(part);
            }
        }
        return result;
    }
}
