import java.util.*;
import java.io.*;

public class C1_P3_Shoe_Shopping {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] shoes = new int[n];
        for (int i = 0; i < n; i++) {
            shoes[i] = 2 * readInt();
        }
        long[] dp = new long[n];
        Arrays.fill(dp, (int) 1e9);
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                dp[i] = Math.min(dp[i], shoes[i]);
            } else {
                dp[i] = Math.min(dp[i], dp[i - 1] + shoes[i]);
            }
            if (i >= 1) {
                long group_2 = Math.min(shoes[i], shoes[i - 1]) / 2 + Math.max(shoes[i], shoes[i - 1]);
                if (i == 1) {
                    dp[i] = Math.min(dp[i], group_2);
                } else {
                    dp[i] = Math.min(dp[i], dp[i - 2] + group_2);
                }
            }
            if (i >= 2) {
                long group_3 = shoes[i] + shoes[i - 1] + shoes[i - 2] - Math.min(shoes[i], Math.min(shoes[i - 1], shoes[i - 2]));
                if (i == 2) {
                    dp[i] = Math.min(dp[i], group_3);
                } else {
                    dp[i] = Math.min(dp[i], dp[i - 3] + group_3);
                }
            }
        }
        System.out.println(dp[n - 1] / 2 + (dp[n - 1] % 2 == 0 ? ".0" : ".5"));
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
