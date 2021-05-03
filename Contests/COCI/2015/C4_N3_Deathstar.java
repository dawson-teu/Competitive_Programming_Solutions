import java.util.*;
import java.io.*;

public class P3_Deathstar {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = readInt();
            }
        }

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < 32; k++) {
                    if (((matrix[i][j] >> (k - 1)) & 1) > 0) {
                        arr[i] = arr[i] | (1 << (k - 1));
                    }
                }
            }
        }
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (i != n - 1) {
                output.append(arr[i]).append(" ");
            } else {
                output.append(arr[i]);
            }
        }
        System.out.println(output);
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
