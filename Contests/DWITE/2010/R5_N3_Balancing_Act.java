import java.util.*;
import java.io.*;

public class R5_N3_Balancing_Act {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        for (int m = 0; m < 5; m++) {
            int n = readInt();
            int[] weights = new int[n];
            int totalSum = 0;
            for (int i = 0; i < n; i++) {
                weights[i] = readInt();
                totalSum += weights[i];
            }

            boolean[] prev = new boolean[totalSum + 1];
            boolean[] cur = new boolean[totalSum + 1];
            prev[0] = true;
            for (int i = 1; i < n; i++) {
                for (int j = 0; j < totalSum + 1; j++) {
                    if (j == 0) {
                        cur[j] = true;
                    } else if (j >= weights[i - 1]) {
                        cur[j] = prev[j - weights[i - 1]] || prev[j];
                    }
                }
                System.arraycopy(cur, 0, prev, 0, cur.length);
            }
            int minDiff = Integer.MAX_VALUE;
            for (int i = 0; i < totalSum + 1; i++) {
                if (prev[i]) {
                    minDiff = Math.min(minDiff, Math.abs(i - (totalSum - i)));
                }
            }
            System.out.println(minDiff);
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
