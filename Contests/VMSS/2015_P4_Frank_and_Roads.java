import java.util.*;
import java.io.*;

public class P6_Frank_and_Roads {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int t = readInt(), n = readInt(), m = readInt(), g = readInt();
        int[] food_basics = new int[g];
        for (int i = 0; i < g; i++) {
            food_basics[i] = readInt();
        }

        List<List<Edge>> adjList = new ArrayList<>();
        for (int i = 0; i < n + 1; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int a = readInt();
            int b = readInt();
            int l = readInt();
            adjList.get(a).add(new Edge(b, l));
        }

        PriorityQueue<Edge> queue = new PriorityQueue<>();
        boolean[] visited = new boolean[n + 1];
        int[] dist = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            dist[i] = (int) 1e9;
        }
        queue.add(new Edge(0, 0));
        dist[0] = 0;

        while (!queue.isEmpty()) {
            Edge vertex = queue.poll();
            visited[vertex.v] = true;
            for (Edge neighbour : adjList.get(vertex.v)) {
                if (!visited[neighbour.v]) {
                    int newDist = dist[vertex.v] + neighbour.w;
                    if (newDist < dist[neighbour.v]) {
                        dist[neighbour.v] = newDist;
                        queue.add(new Edge(neighbour.v, dist[neighbour.v]));
                    }
                }
            }
        }

        int count = 0;
        for (int store: food_basics) {
            if (dist[store] <= t) {
                count += 1;
            }
        }
        System.out.println(count);
    }

    static class Edge implements Comparable<Edge> {
        final int v;
        final int w;

        Edge(int v, int w) {
            this.v = v;
            this.w = w;
        }

        public int compareTo(Edge o) {
            return Integer.compare(w, o.w);
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
