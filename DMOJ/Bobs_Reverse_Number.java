import java.util.*;
import java.io.*;

public class Bobs_Reverse_Number {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        long a = readLong(), b = readLong();
        a = Long.parseLong(new StringBuilder(String.valueOf(a)).reverse().toString());
        b = Long.parseLong(new StringBuilder(String.valueOf(b)).reverse().toString());
        System.out.println(Math.min(a, b));
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
