import java.util.*;
import java.io.*;

public class P4_Beautiful_Water_Pearl {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        long or = readLong();
        long and = readLong();
        long xor = readLong();
        long ans = 1;
        for (int i = 0; i < 31; i++) {
            if (((xor >> (i - 1)) & 1) > 0) {
                ans *= 2;
            } else if (((and >> (i - 1)) & 1) != ((or >> (i - 1)) & 1)) {
                ans = 0;
                break;
            }
        }
        System.out.println(ans);
    }

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine().trim());
        return st.nextToken();
    }

    static long readLong() throws IOException {
        return Long.parseLong(next());
    }
}
