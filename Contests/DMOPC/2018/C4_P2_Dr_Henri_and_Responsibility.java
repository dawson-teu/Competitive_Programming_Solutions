import java.util.*;
import java.io.*;

public class P3_Dr_Henri_and_Responsibility {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] a = new int[n];
        int totalSum = 0;
        for (int i = 0; i < n; i++) {
            a[i] = readInt();
            totalSum += a[i];
        }

        boolean[] prev = new boolean[totalSum + 1];
        boolean[] cur = new boolean[totalSum + 1];
        prev[0] = true;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < totalSum + 1; j++) {
                if (j == 0) {
                    cur[j] = true;
                } else if (j >= a[i - 1]) {
                    cur[j] = prev[j - a[i - 1]] || prev[j];
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

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine().trim());
        return st.nextToken();
    }

    static int readInt() throws IOException {
        return Integer.parseInt(next());
    }
}
