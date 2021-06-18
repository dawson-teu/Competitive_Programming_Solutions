import java.util.*;
import java.io.*;

public class Gift_Division {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] gifts = new int[n];
        int totalSum = 0;
        for (int i = 0; i < n; i++) {
            gifts[i] = readInt();
            totalSum += gifts[i];
        }
        int maxBagSize = 2000 / 3 + 1;
        boolean[][][] dp = new boolean[n + 1][maxBagSize + 1][maxBagSize + 1];
        dp[0][0][0] = true;
        for (int i = 1; i < n + 1; i++) {
            for (int j = 0; j < maxBagSize + 1; j++) {
                for (int k = 0; k < maxBagSize + 1; k++) {
                    dp[i][j][k] = dp[i - 1][j][k];
                    if (j - gifts[i - 1] >= 0) {
                        dp[i][j][k] = dp[i][j][k] || dp[i - 1][j - gifts[i - 1]][k];
                    }
                    if (k - gifts[i - 1] >= 0) {
                        dp[i][j][k] = dp[i][j][k] || dp[i - 1][j][k - gifts[i - 1]];
                    }
                }
            }
        }
        int ans = (int) 1e9;
        for (int i = 0; i < maxBagSize + 1; i++) {
            for (int j = 0; j < maxBagSize + 1; j++) {
                if (dp[n][i][j]) {
                    ans = Math.min(ans, Math.max(i, Math.max(j, totalSum - i - j)));
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
