import java.util.*;
import java.io.*;

public class P8_Knapsack_2 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), w = readInt();
        int[] value = new int[n];
        int[] weights = new int[n];
        int valueSum = 0;
        for (int i = 0; i < n; i++) {
            weights[i] = readInt();
            value[i] = readInt();
            valueSum += value[i];
        }

        long[] prev = new long[valueSum + 1];
        long[] cur = new long[valueSum + 1];
        Arrays.fill(prev, (long) 1e9);
        prev[0] = 0;
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < valueSum + 1; j++) {
                if (value[i - 1] <= j) {
                    cur[j] = Math.min(prev[j], prev[j - value[i - 1]] + weights[i - 1]);
                } else {
                    cur[j] = prev[j];
                }
            }
            prev = Arrays.copyOf(cur, cur.length);
        }

        int maxValue = 0;
        for (int j = 1; j < valueSum + 1; j++) {
            if (cur[j] <= w) {
                maxValue = Math.max(maxValue, j);
            }
        }
        System.out.println(maxValue);
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

