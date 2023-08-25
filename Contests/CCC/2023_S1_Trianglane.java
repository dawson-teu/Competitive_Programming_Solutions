import java.util.*;
import java.io.*;

public class S1_Trianglane {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int c = readInt();

        int[][] tiles = new int[2][c];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < c; j++) {
                tiles[i][j] = readInt();
            }
        }

        int total = 0;
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < c; j++) {
                if (tiles[i][j] == 0) {
                    continue;
                }

                int numNeighbours = 0;
                if (j > 0) {
                    numNeighbours += tiles[i][j - 1];
                }
                if (j < c - 1) {
                    numNeighbours += tiles[i][j + 1];
                }
                if (i == 0 && j % 2 == 0) {
                    numNeighbours += tiles[1][j];
                } else if (i == 1 && j % 2 == 0){
                    numNeighbours += tiles[0][j];
                }

                total += 3 - numNeighbours;
            }
        }

        System.out.println(total);
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
