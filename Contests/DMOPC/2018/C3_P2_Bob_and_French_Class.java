import java.util.*;
import java.io.*;

public class C3_P2_Bob_and_French_Class {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] a = new int[n];
        int[] b = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = readInt();
        }
        for (int i = 0; i < n; i++) {
            b[i] = readInt();
        }
        int[][] dp = new int[n + 1][3];
        for (int i = 1; i <= n; i++) {
            dp[i][2] = dp[i - 1][1] + a[i - 1];
            dp[i][1] = dp[i - 1][0] + a[i - 1];
            dp[i][0] = Math.max(Math.max(dp[i - 1][0], dp[i - 1][1]), dp[i - 1][2]) + b[i - 1];
        }
        System.out.println(Math.max(Math.max(dp[n][0], dp[n][1]), dp[n][2]));
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
