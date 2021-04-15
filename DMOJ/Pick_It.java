import java.util.*;
import java.io.*;

public class P7_Pick_It {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        while (n != 0) {
            int[] nums = new int[n];
            for (int i = 0; i < n; i++) {
                nums[i] = readInt();
            }
            int[][] dp = new int[n][n];
            for (int i = 0; i < n - 1; i++) {
                dp[i][i + 1] = 0;
            }
            for (int len = 2; len < n; len++) {
                for (int i = 0; i + len < n; i++) {
                    int j = i + len;
                    for (int k = i + 1; k < j; k++) {
                        int newScore = nums[i] + nums[j] + nums[k] + dp[i][k] + dp[k][j];
                        dp[i][j] = Math.max(dp[i][j], newScore);
                    }
                }
            }
            System.out.println(dp[0][n - 1]);

            n = readInt();
        }
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
