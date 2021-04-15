import java.util.*;
import java.io.*;

public class P4_Deque {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] values = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = readInt();
        }
        long[] psa = new long[n + 1];
        psa[0] = 0;
        for (int i = 0; i < n; i++) {
            psa[i + 1] = psa[i] + values[i];
        }

        long[][] dp = new long[n][n];
        for (int i = 0; i < n; i++) {
            dp[i][i] = values[i];
        }
        for (int len = 1; len < n; len++) {
            for (int i = 0; i + len < n; i++) {
                int j = i + len;
                dp[i][j] = Math.max(psa[j + 1] - psa[i] - dp[i + 1][j], psa[j + 1] - psa[i] - dp[i][j - 1]);
            }
        }
        System.out.println(2 * dp[0][n - 1] - psa[n]);
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
