import java.util.*;
import java.io.*;

public class Coding_Spree {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), w = readInt();
        int[] value = new int[n];
        int[] weights = new int[n];
        for (int i = 0; i < n; i++) {
            value[i] = readInt();
            weights[i] = readInt();
        }

        long[] prev = new long[w + 1];
        long[] cur = new long[w + 1];
        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < w + 1; j++) {
                if (i == 0 || j == 0) {
                    cur[j] = 0;
                } else if (weights[i - 1] <= j) {
                    cur[j] = Math.max(prev[j - weights[i - 1]] + value[i - 1], prev[j]);
                } else {
                    cur[j] = prev[j];
                }
            }
            prev = Arrays.copyOf(cur, cur.length);
        }
        System.out.println(cur[w]);
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
