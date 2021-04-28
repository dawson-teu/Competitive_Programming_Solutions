import java.util.*;
import java.io.*;

public class Dec_B1_Do_You_Know_Your_ABCs {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int[] list = new int[7];
        for (int i = 0; i < 7; i++) {
            list[i] = readInt();
        }
        Arrays.sort(list);
        int a = list[0];
        int b = list[1];
        int c = list[6] - a - b;
        System.out.println(a + " " + b + " " + c);
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
