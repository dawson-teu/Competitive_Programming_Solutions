import java.util.*;
import java.io.*;

public class Dans_Coin_Problem {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int t = readInt();
        for (int m = 0; m < t; m++) {
            int n = readInt();
            int[] denoms = new int[n];
            int max_denom = -1;
            for (int i = 0; i < n; i++) {
                denoms[i] = readInt();
                max_denom = Math.max(denoms[i], max_denom);
            }
            Arrays.sort(denoms);

            boolean[] dp = new boolean[max_denom + 1];
            dp[0] = true;
            int total = 0;
            for (int i = 0; i < n; i++) {
                boolean is_collision = false;
                for (int j = 0; j < dp.length; j++) {
                    if (denoms[i] > j) {
                        continue;
                    }
                    if (dp[j] && j == denoms[i]) {
                        is_collision = true;
                    }
                    if (dp[j - denoms[i]]) {
                        dp[j] = true;
                    }
                }
                if (!is_collision) {
                    total += 1;
                }
            }
            System.out.println(total);
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
