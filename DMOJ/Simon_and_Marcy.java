import java.util.*;
import java.io.*;

public class P1_Simon_and_Marcy {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int c = readInt(), m = readInt();
        int[] value = new int[c];
        int[] weights = new int[c];
        for (int i = 0; i < c; i++) {
            value[i] = readInt();
            weights[i] = readInt();
        }
        
        int[][] dp = new int[c + 1][m + 1];
        for (int i = 0; i < c + 1; i++) {
            for (int j = 0; j < m + 1; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 0;
                } else if (weights[i - 1] <= j) {
                    dp[i][j] = Math.max(dp[i - 1][j - weights[i - 1]] + value[i - 1], dp[i - 1][j]);
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        System.out.println(dp[c][m]);
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
