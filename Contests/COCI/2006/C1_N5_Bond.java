import java.util.*;
import java.io.*;

public class C1_N5_Bond {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int n;
    static double[] dp;
    static double[][] probs;
    public static void main(String[] args) throws IOException {
        n = readInt();
        probs = new double[n][n];
        dp = new double[1 << n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                probs[i][j] = readInt() / 100.0;
            }
        }
        System.out.printf("%.9f", max_prob(0, 0) * 100);
    }

    static double max_prob(int bond, int mask) {
        if (dp[mask] > 0) {
            return dp[mask];
        }
        if (bond >= n) {
            return 1;
        }
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) == 0) {
                dp[mask] = Math.max(dp[mask], probs[bond][i] * max_prob(bond + 1, mask | (1 << i)));
            }
        }
        return dp[mask];
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
