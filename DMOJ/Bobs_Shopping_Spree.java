import java.util.*;
import java.io.*;

public class Bobs_Shopping_Spree {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt(), k = readInt();
        long[] unWeights = new long[n];
        long[] unValues = new long[n];
        for (int i = 0; i < n; i++) {
            unWeights[i] = readInt();
            unValues[i] = readInt();
        }
        long[] limWeights = new long[m];
        long[] limValues = new long[m];
        long[] limits = new long[m];
        for (int i = 0; i < m; i++) {
            int q = readInt(), t = readInt();
            limWeights[i] = readInt();
            limValues[i] = q * unValues[t - 1];
            limits[i] = readInt();
        }
        long[] dp = new long[1100];
        for (int i = 0; i < n; i++) {
            for (int j = (int) unWeights[i]; j <= k; j++) {
                dp[j] = Math.max(dp[j], dp[j - (int) unWeights[i]] + unValues[i]);
            }
        }
        for (int i = 0; i < m; i++) {
            int power = 1;
            while (power < limits[i]) {
                for (int j = k; j >= limWeights[i] * power; j--) {
                    dp[j] = Math.max(dp[j - (int) limWeights[i] * power] + limValues[i] * power, dp[j]);
                }
                limits[i] -= power;
                power *= 2;
            }
            if (limits[i] > 0) {
                for (int j = k; j >= limWeights[i] * limits[i]; j--) {
                    dp[j] = Math.max(dp[(int) (j - limWeights[i] * limits[i])] + limValues[i] * limits[i], dp[j]);
                }
            }
        }
        System.out.println(dp[k]);
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
