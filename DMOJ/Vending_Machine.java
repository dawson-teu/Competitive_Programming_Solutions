import java.util.*;
import java.io.*;

public class Vending_Machine {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), c = readInt();
        int[] weights1 = new int[n];
        int[] values1 = new int[n];
        int[] weights2 = new int[n];
        int[] values2 = new int[n];
        for (int i = 0; i < n; i++) {
            weights1[i] = readInt();
            values1[i] = readInt();
            weights2[i] = readInt();
            values2[i] = readInt();
        }
        long[][][] dp = new long[2][n + 1][c + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= c; j++) {
                if (weights1[i - 1] <= j) {
                    dp[0][i][j] = Math.max(Math.max(dp[0][i - 1][j], dp[1][i - 1][j]), dp[1][i][j - weights1[i - 1]] + values1[i - 1]);
                } else {
                    dp[0][i][j] = Math.max(dp[0][i - 1][j], dp[1][i - 1][j]);
                }
                if (weights2[i - 1] <= j) {
                    dp[1][i][j] = Math.max(Math.max(dp[0][i - 1][j], dp[1][i - 1][j]), dp[0][i][j - weights2[i - 1]] + values2[i - 1]);
                } else {
                    dp[1][i][j] = Math.max(dp[0][i - 1][j], dp[1][i - 1][j]);
                }
            }
        }
        System.out.println(Math.max(dp[0][n][c], dp[1][n][c]));
    }

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine().trim());
        return st.nextToken();
    }

    static int readInt() throws IOException {
        return Integer.parseInt(next());
    }
}
