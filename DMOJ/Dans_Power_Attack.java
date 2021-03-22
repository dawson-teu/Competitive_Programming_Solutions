import java.util.*;
import java.io.*;

public class Dans_Power_Attack {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), d = readInt(), k = readInt();
        int[] healths = new int[n];
        for (int i = 0; i < n; i++) {
            healths[i] = readInt();
        }
        Arrays.sort(healths);
        int count = 0;
        long total = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (count >= k) {
                if (healths[i] % d == 0) {
                    total += healths[i] / d;
                } else {
                    total += healths[i] / d + 1;
                }
            }
            count += 1;
        }
        System.out.println(total);
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
