import java.util.*;
import java.io.*;

public class P8_Combining_Riceballs {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] psa = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            psa[i] = psa[i - 1] + readInt();
        }

        boolean[][] dp = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
        }

        for (int len = 1; len < n; len++) {
            for (int i = 0; i + len < n; i++) {
                int j = i + len;
                for (int k = i; k <= j; k++) {
                    if (dp[i][k] && dp[k + 1][j] && psa[k + 1] - psa[i] == psa[j + 1] - psa[k + 1]) {
                        dp[i][j] = true;
                        break;
                    }
                }
                if (dp[i][j]) {
                    continue;
                }
                int p = i, q = j;
                while (p < q) {
                    if (dp[i][p] && dp[q][j] && dp[p + 1][q - 1] && psa[p + 1] - psa[i] == psa[j + 1] - psa[q]) {
                        dp[i][j] = true;
                        break;
                    }
                    if (psa[p + 1] - psa[i] > psa[j + 1] - psa[q]) {
                        q -= 1;
                    } else {
                        p += 1;
                    }
                }
            }
        }
        int ans = -1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dp[i][j]) {
                    ans = Math.max(ans, psa[j + 1] - psa[i]);
                }
            }
        }
        System.out.println(ans);
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
