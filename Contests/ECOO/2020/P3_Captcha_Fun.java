import java.util.*;

public class CaptchaFun {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int t = input.nextInt();
        for (int i = 0; i < t; i++) {
            int n = input.nextInt();
            StringBuilder ans = new StringBuilder();
            for (int j = 0; j < n; j++) {
                int h = input.nextInt();
                int w = input.nextInt();
                int[] ast = new int[h];
                int[] right = new int[h];
                int top = h;
                int bottom = h;
                input.nextLine();
                for (int r = 0; r < h; r++) {
                    String line = input.nextLine();
                    for (int c = 0; c < w; c++) {
                        if (line.charAt(c) == '*') {
                            ast[r] += 1;
                            right[r] = c;
                            top = Math.min(top, r);
                            bottom = Math.max(top, r);
                        }
                    }
                }
                int mid = (top + bottom + 1) / 2;
                if (ast[mid] == 0) {
                    if (mid - top != bottom - mid) {
                        ans.append("7");
                    } else if (ast[mid - 1] == 2) {
                        ans.append("0");
                    } else {
                        ans.append("1");
                    }
                } else {
                    if (ast[top] != ast[bottom]) {
                        ans.append("4");
                    } else if (ast[top + 1] == 2 && ast[bottom - 1] == 2) {
                        ans.append("8");
                    } else if (ast[top + 1] == 2) {
                        ans.append("9");
                    } else if (ast[bottom - 1] == 2) {
                        ans.append("6");
                    } else if (right[top + 1] == right[bottom - 1]) {
                        ans.append("3");
                    } else if (right[top + 1] < right[bottom - 1]) {
                        ans.append("5");
                    } else {
                        ans.append("2");
                    }
                }
            }
            System.out.println(ans);
        }
    }
}
