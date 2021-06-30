import java.util.*;
import java.io.*;

public class P1_Geese_vs_Hawks {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        boolean[] aResult = new boolean[n];
        String line = readLine();
        for (int i = 0; i < n; i++) {
            aResult[i] = (line.charAt(i) == 'W');
        }
        int[] aPoints = new int[n];
        for (int i = 0; i < n; i++) {
            aPoints[i] = readInt();
        }

        boolean[] bResult = new boolean[n];
        line = readLine();
        for (int i = 0; i < n; i++) {
            bResult[i] = (line.charAt(i) == 'W');
        }
        int[] bPoints = new int[n];
        for (int i = 0; i < n; i++) {
            bPoints[i] = readInt();
        }
        int[][] dp = new int[n + 1][n + 1];
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                int prevMax = Math.max(dp[i - 1][j], dp[i][j - 1]);
                boolean aWins = aResult[i - 1] && !bResult[j - 1] && aPoints[i - 1] > bPoints[j - 1];
                boolean bWins = !aResult[i - 1] && bResult[j - 1] && aPoints[i - 1] < bPoints[j - 1];
                if (aWins || bWins) {
                    dp[i][j] = Math.max(prevMax, dp[i - 1][j - 1] + aPoints[i - 1] + bPoints[j - 1]);
                } else {
                    dp[i][j] = prevMax;
                }
            }
        }
        System.out.println(dp[n][n]);
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
