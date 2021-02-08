import java.util.*;
import java.io.*;

public class P7_Spaced_Out {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt();
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = readInt();
            }
        }

        int maxHorizontal = 0;
        for (int i = 0; i < n; i++) {
            int evenSum = 0, oddSum = 0;
            for (int j = 0; j < n; j++) {
                if (j % 2 == 0) {
                    evenSum += grid[i][j];
                } else {
                    oddSum += grid[i][j];
                }
            }
            maxHorizontal += Math.max(evenSum, oddSum);
        }

        int maxVertical= 0;
        for (int i = 0; i < n; i++) {
            int evenSum = 0, oddSum = 0;
            for (int j = 0; j < n; j++) {
                if (j % 2 == 0) {
                    evenSum += grid[j][i];
                } else {
                    oddSum += grid[j][i];
                }
            }
            maxVertical += Math.max(evenSum, oddSum);
        }

        System.out.println(Math.max(maxHorizontal, maxVertical));
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
