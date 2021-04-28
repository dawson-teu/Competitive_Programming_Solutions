import java.util.*;
import java.io.*;

public class S4_Shop_and_Ship {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), t = readInt();
        int[][] adjMat = new int[n][n];
        for (int i = 0; i < t; i++) {
            int x = readInt(), y = readInt(), c = readInt();
            adjMat[x - 1][y - 1] = c;
            adjMat[y - 1][x - 1] = c;
        }

        int k = readInt();
        int[] pencilCity = new int[k];
        int[] pencilCost = new int[k];
        for (int i = 0; i < k; i++) {
            pencilCity[i] = readInt();
            pencilCost[i] = readInt();
        }

        int d = readInt();
        int[] dist = new int[n];
        Arrays.fill(dist, (int) 1e10);
        boolean[] visited = new boolean[n];
        dist[d - 1] = 0;
        for (int i = 0; i < n; i++) {
            int min = Integer.MAX_VALUE, vertex = -1;
            for (int j = 0; j < n; j++) {
                if (!visited[j] && dist[j] < min) {
                    min = dist[j];
                    vertex = j;
                }
            }
            if (vertex == -1) {
                break;
            }
            visited[vertex] = true;
            for (int neighbour = 0; neighbour < n; neighbour++) {
                if (adjMat[vertex][neighbour] == 0) {
                    continue;
                }
                int newDist = dist[vertex] + adjMat[vertex][neighbour];
                if (!visited[neighbour] && newDist < dist[neighbour]) {
                    dist[neighbour] = newDist;
                }
            }
        }
        int minCost = Integer.MAX_VALUE;
        for (int i = 0; i < k; i++) {
            minCost = Math.min(minCost, dist[pencilCity[i] - 1] + pencilCost[i]);
        }
        System.out.println(minCost);
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
