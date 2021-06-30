import java.util.*;
import java.io.*;

public class Chicken_and_Rabbit {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int x = readInt(), y = readInt();
        if (y % 2 == 0 && 2 * x - y / 2 >= 0 && y / 2 - x >= 0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
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
