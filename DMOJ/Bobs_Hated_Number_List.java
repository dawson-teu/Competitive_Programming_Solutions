import java.util.*;
import java.io.*;

public class Bobs_Hated_Number_List {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int x = readInt(), n = readInt();
        Set<Integer> hatedNumber = new HashSet<>();
        for (int i = 0; i < n; i++) {
            hatedNumber.add(readInt());
        }
        int left = x;
        while (true) {
            if (hatedNumber.contains(left)) {
                left -= 1;
            } else {
                break;
            }
        }
        int right = x;
        while (true) {
            if (hatedNumber.contains(right)) {
                right += 1;
            } else {
                break;
            }
        }
        if (right - x < x - left) {
            System.out.println(right);
        } else {
            System.out.println(left);
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
