import java.util.*;
import java.io.*;

public class P2_Vacation {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();

        int[] a = new int[n];
        int[] b = new int[n];
        int[] c = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = readInt();
            b[i] = readInt();
            c[i] = readInt();
        }

        int[][] dp = new int[n][3];
        dp[0][0] = a[0];
        dp[0][1] = b[0];
        dp[0][2] = c[0];
        for (int i = 1; i < n; i++) {
            dp[i][0] = a[i] + Math.max(dp[i - 1][1], dp[i - 1][2]);
            dp[i][1] = b[i] + Math.max(dp[i - 1][0], dp[i - 1][2]);
            dp[i][2] = c[i] + Math.max(dp[i - 1][0], dp[i - 1][1]);
        }
        System.out.println(Math.max(dp[n - 1][2], Math.max(dp[n - 1][0], dp[n - 1][1])));
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
