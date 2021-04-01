import java.util.*;
import java.io.*;

public class P3_Bobs_Video_Game {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt(), t = readInt();
        int[][] adjMat = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(adjMat[i], Integer.MAX_VALUE);
        }
        for (int i = 0; i < m; i++) {
            int s = readInt(), e = readInt(), h = readInt();
            adjMat[s - 1][e - 1] = h;
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    adjMat[i][j] = Math.min(adjMat[i][j], Math.max(adjMat[i][k], adjMat[k][j]));
                }
            }
        }
        for (int i = 0; i < t; i++) {
            int a = readInt(), b = readInt();
            if (adjMat[a - 1][b - 1] == Integer.MAX_VALUE) {
                System.out.println("-1");
            } else {
                System.out.println(adjMat[a - 1][b - 1]);
            }
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
