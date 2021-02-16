import java.util.*;
import java.io.*;

public class P6_Troyangles {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        boolean[][] grid = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            String line = readLine();
            for (int j = 0; j < n; j++) {
                grid[i][j] = line.charAt(j) == '#';
            }
        }
        int[][] dp = new int[n][n];
        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j]) {
                    if (j > 0 && j < n - 1 && i < n - 1) {
                        dp[i][j] = Math.min(dp[i + 1][j - 1], dp[i + 1][j]);
                        dp[i][j] = Math.min(dp[i][j], dp[i + 1][j + 1]) + 1;
                    } else {
                        dp[i][j] = 1;
                    }
                }
            }
        }
        int sum = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sum += dp[i][j];
            }
        }
        System.out.println(sum);
    }

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine().trim());
        return st.nextToken();
    }

    static int readInt() throws IOException {
        return Integer.parseInt(next());
    }

    static String readLine() throws IOException {
        return br.readLine().trim();
    }
}
