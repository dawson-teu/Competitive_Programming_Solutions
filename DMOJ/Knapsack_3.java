import java.util.*;
import java.io.*;

public class P8_Knapsack_3 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        long[] dp = new long[5001];
        for (int i = 1; i < n + 1; i++) {
            int num = readInt(), weight = readInt(), value = readInt();
            long cur_power = 1;
            long cur_num = num;
            while (cur_power <= cur_num) {
                long cur_weight = weight * cur_power, cur_value = value * cur_power;
                for (int j = 5000; j >= cur_weight; j--) {
                    dp[j] = Math.max(dp[(int) (j - cur_weight)] + cur_value, dp[j]);
                }
                cur_num -= cur_power;
                cur_power *= 2;
            }
            if (cur_num > 0) {
                long cur_weight = weight * cur_num, cur_value = value * cur_num;
                for (int j = 5000; j >= cur_weight; j--) {
                    dp[j] = Math.max(dp[(int) (j - cur_weight)] + cur_value, dp[j]);
                }
            }
        }
        long cur_ans = Long.MIN_VALUE;
        for (int i = 0; i < m; i++) {
            int size = readInt(), fuel = readInt();
            cur_ans = Math.max(cur_ans, dp[size] - fuel);
        }
        System.out.println(cur_ans);
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
