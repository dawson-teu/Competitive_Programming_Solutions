import java.util.*;
import java.io.*;

public class S5_Bowling_for_Numbers {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int t = readInt();
        for (int i = 0; i < t; i++) {
            int n = readInt(), k = readInt(), w = readInt();
            int[] scores = new int[n];
            for (int j = 0; j < n; j++) {
                scores[j] = readInt();
            }
            int[] psa = new int[n + 1];
            psa[0] = 0;
            for (int j = 0; j < n; j++) {
                psa[j + 1] = psa[j] + scores[j];
            }
            int[][] dp = new int[k + 1][n];
            for (int j = 1; j < k + 1; j++) {
                for (int m = 0; m < n; m++) {
                    if (m >= w) {
                        dp[j][m] = Math.max(dp[j - 1][m - w] + psa[m + 1] - psa[m - w + 1], dp[j][m - 1]);
                    } else if (m >= 1) {
                        dp[j][m] = Math.max(psa[m + 1], dp[j][m - 1]);
                    } else {
                        dp[j][m] = psa[m + 1];
                    }
                }
            }
            System.out.println(dp[k][n - 1]);
        }
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
