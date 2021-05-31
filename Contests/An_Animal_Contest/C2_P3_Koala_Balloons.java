import java.util.*;
import java.io.*;

public class C2_P3_Koala_Balloons {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        int[][] grid = new int[n][m];
        for (int i = 0; i < n; i++) {
            String line = readLine();
            for (int j = 0; j < m; j++) {
                if (line.charAt(j) == 'X') {
                    grid[i][j] = 1;
                }
            }
        }
        int[][] psa = new int[n + 1][m + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                psa[i + 1][j + 1] = -psa[i][j] + psa[i + 1][j] + psa[i][j + 1] + grid[i][j];
            }
        }
        int low = 1;
        int high = Math.min(n, m);
        int ans = 0;
        while (low <= high) {
            int i = (low + high) / 2;
            if (psa[i][i] - psa[i][0] - psa[0][i] == 0 && bfs(grid, psa, i)) {
                ans = i;
                low = i + 1;
            } else {
                high = i - 1;
            }
        }
        System.out.println(ans);
    }

    static boolean bfs(int[][] grid, int[][] psa, int size) {
        int n = grid.length;
        int m = grid[0].length;
        boolean[][] visited = new boolean[n][m];
        Queue<Pair> queue = new LinkedList<>();
        queue.add(new Pair(0, 0));
        visited[0][0] = true;
        while (!queue.isEmpty()) {
            Pair pos = queue.poll();
            if (pos.x == m - size && pos.y == n - size) {
                return true;
            }
            int[] change = {0, 1, 0, -1, 1, 0, -1, 0};
            for (int i = 0; i < 8; i += 2) {
                int newX = pos.x + change[i];
                int newY = pos.y + change[i + 1];
                if (!(0 <= newX && newX < (grid[0].length - size + 1) && 0 <= newY && newY < (grid.length - size + 1) && grid[newY][newX] == 0)) {
                    continue;
                }
                int count = psa[newY + size][newX + size] - psa[newY][newX + size] - psa[newY + size][newX] + psa[newY][newX];
                if (!visited[newY][newX] && count == 0) {
                    queue.add(new Pair(newX, newY));
                    visited[newY][newX] = true;
                }
            }
        }
        return false;
    }

    static class Pair {
        final int x;
        final int y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
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

    static String readLine() throws IOException {
        return br.readLine().trim();
    }
}
