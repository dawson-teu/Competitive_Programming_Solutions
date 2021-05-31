import java.util.*;
import java.io.*;

public class C3_P5_Not_Enough_Servers {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        int[] testCases = new int[m];
        int subResults = 0;
        for (int i = 0; i < n; i++) {
            String subs = readLine();
            int subResult = 0;
            for (int j = 0; j < m; j++) {
                if (subs.charAt(j) == 'X') {
                    testCases[j] = testCases[j] | (1 << n - i - 1);
                    subResult = subResult | 1;
                }
            }
            subResults = subResults | (subResult << n - i - 1);
        }

        if (subResults == 0) {
            System.out.println(1);
            System.out.println(1);
        } else {
            int[] dp = new int[1 << n];
            int[] caseKey = new int[1 << n];
            int[] prev = new int[1 << n];
            Arrays.fill(dp, (int) 1e9);
            Arrays.fill(prev, -1);
            dp[0] = 0;
            for (int i = 0; i < m; i++) {
                for (int mask = 0; mask < 1 << n; mask++) {
                    if (dp[mask | testCases[i]] > dp[mask] + 1) {
                        dp[mask | testCases[i]] = dp[mask] + 1;
                        caseKey[mask | testCases[i]] = i + 1;
                        prev[mask | testCases[i]] = mask;
                    }
                }
            }
            System.out.println(dp[subResults]);
            int curMask = subResults;
            StringBuilder output = new StringBuilder();
            while (prev[curMask] != -1) {
                output.append(caseKey[curMask]).append(" ");
                curMask = prev[curMask];
            }
            System.out.println(output);
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

    static String readLine() throws IOException {
        return br.readLine().trim();
    }
}
