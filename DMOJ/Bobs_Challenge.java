import java.util.*;
import java.io.*;

public class Bobs_Challenge {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        long pow_2 = 1;
        long[] dp = new long[n + 1];
        dp[0] = 1;
        while (pow_2 < n) {
            for (int i = 1; i <= n; i++) {
                if (i - pow_2 >= 0) {
                    dp[i] += dp[i - (int) pow_2];
                    dp[i] %= (int) (1e9 + 7);
                }
            }
            pow_2 *= 2;
        }
        System.out.println(dp[n] % (int) (1e9 + 7));
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
