import java.util.*;
import java.io.*;

public class P4_Migrant_Mascot {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = readInt(), m = readInt();
        List<List<Edge>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int a = readInt();
            int b = readInt();
            int p = readInt();
            adjList.get(a - 1).add(new Edge(b, p));
            adjList.get(b - 1).add(new Edge(a, p));
        }

        PriorityQueue<Edge> queue = new PriorityQueue<>();
        boolean[] visited = new boolean[n];
        int[] dist = new int[n];
        dist[0] = (int) 1e9;
        queue.add(new Edge(0, dist[0]));

        while (!queue.isEmpty()) {
            Edge vertex = queue.poll();
            visited[vertex.v - 1] = true;

            for (Edge neighbour : adjList.get(vertex.v - 1)) {
                if (!visited[neighbour.v - 1]) {
                    int min_dist = Math.min(dist[vertex.v - 1], neighbour.w);
                    if (dist[neighbour.v - 1] < min_dist) {
                        dist[neighbour.v - 1] = min_dist;
                        queue.add(new Edge(neighbour.v, dist[neighbour.v - 1]));
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (i == 0) {
                System.out.println(0);
            } else {
                System.out.println(dist[i]);
            }
        }
    }

    static class Edge implements Comparable<Edge> {
        final int v;
        final int w;

        Edge(int v, int w) {
            this.v = v;
            this.w = w;
        }

        public int compareTo(Edge o) {
            return Integer.compare(o.w, w);
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
