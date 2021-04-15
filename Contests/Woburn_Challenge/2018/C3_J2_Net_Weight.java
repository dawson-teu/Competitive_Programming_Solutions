import java.util.*;
import java.io.*;

public class P1_Net_Weight {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[] weights = new int[n];
        for (int i = 0 ; i < n; i++) {
            weights[i] = readInt();
            if (weights[i] > 100) {
                weights[i] = 0;
            }
        }
        Arrays.sort(weights);
        if (weights.length == 1) {
            System.out.println(weights[0]);
        } else {
            System.out.println(weights[weights.length - 1] + weights[weights.length - 2]);
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
