import java.io.*;
import java.util.*;

public class P1_Palindrome {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[][] dp = new int[2][n + 1];
        String str_for = readLine();
        String str_back = new StringBuilder().append(str_for).reverse().toString();
        int previous = 0;
        int current = 1;
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 || j == 0) {
                    dp[current][j] = 0;
                } else if (str_for.charAt(i - 1) == str_back.charAt(j - 1)) {
                    dp[current][j] = dp[previous][j - 1] + 1;
                } else {
                    dp[current][j] = Math.max(dp[current][j - 1], dp[previous][j]);
                }
            }
            int tmp = previous;
            previous = current;
            current = tmp;
        }
        System.out.println(n - dp[previous][n]);
    }

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine().trim());
        return st.nextToken();
    }

    static int readInt() throws IOException {
        return Integer.parseInt(next());
    }

    static String readLine() throws IOException {
        return br.readLine().trim();
    }
}
