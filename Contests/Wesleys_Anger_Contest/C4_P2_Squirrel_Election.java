import java.util.*;
import java.io.*;

public class P3_Squirrel_Election {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] weights = new int[n];
        int[] value = new int[n];
        int valueSum = 0;
        for (int i = 0; i < n; i++) {
            weights[i] = readInt() / 2 + 1;
            value[i] = readInt();
            valueSum += value[i];
        }

        long[][] dp = new long[n + 1][valueSum + 1];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], (long) 1e12);
        }
        dp[0][0] = 0;
        for (int i = 1; i < n + 1; i++) {
            for (int j = 0; j < valueSum + 1; j++) {
                if (value[i - 1] <= j) {
                    dp[i][j] = Math.min(dp[i - 1][j], dp[i - 1][j - value[i - 1]] + weights[i - 1]);
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        long minWeight = (long) 1e12;
        for (int i = valueSum / 2 + 1; i <= valueSum; i++) {
            minWeight = Math.min(minWeight, dp[n][i]);
        }
        System.out.println(minWeight);
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
