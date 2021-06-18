import java.util.*;
import java.io.*;

public class Bobs_Cards {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int cur = 0;
        for (int i = 0; i < n; i++) {
            int num = readInt();
            if (num == cur + 1) {
                cur += 1;
            }
        }
        if (cur == 0) {
            System.out.println(-1);
        } else {
            System.out.println(n - cur);
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
