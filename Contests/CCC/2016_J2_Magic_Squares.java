import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

class J2_Magic_Squares {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int[][] square = new int[4][4];
        for (int i = 0; i < 4; i++) {
            String[] line = input.nextLine().split(" ");
            for (int j = 0; j < 4; j++) {
                square[i][j] = Integer.parseInt(line[j]);
            }
        }
        input.close();

        List<Integer> totals = new ArrayList<>();
        totals.addAll(rowTotal(square));
        totals.addAll(columnTotal(square));

        int total = totals.get(0);
        boolean flag = true;
        for (int elem: totals) {
            if (elem != total) {
                System.out.println("not magic");
                flag = false;
                break;
            }
        }
        if (flag) {
            System.out.println("magic");
        }
    }

    private static List<Integer> rowTotal(int[][] square) {
        List<Integer> rowTotal = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            int total = 0;
            for (int j = 0; j < 4; j++) {
                total += square[i][j];
            }
            rowTotal.add(total);
        }
        return rowTotal;
    }

    private static List<Integer> columnTotal(int[][] square) {
        List<Integer> columnTotal = new ArrayList<>();
        for (int j = 0; j < 4; j++) {
            int total = 0;
            for (int i = 0; i < 4; i++) {
                total += square[i][j];
            }
            columnTotal.add(total);
        }
        return columnTotal;
    }
}
