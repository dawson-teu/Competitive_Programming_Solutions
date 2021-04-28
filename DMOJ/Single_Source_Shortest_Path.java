import java.io.*;
import java.util.*;

public class Single_Source_Shortest_Path {
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int n;
    static List<List<Edge>> adj_list;

    public static void main(String[] args) throws IOException {
        n = readInt();
        int m = readInt();
        adj_list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj_list.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int u = readInt(), v = readInt(), w = readInt();
            boolean a = adj_list.get(u - 1).contains(new Edge(v, w));
            boolean b = adj_list.get(v - 1).contains(new Edge(u, w));
            if (!a && !b) {
                adj_list.get(u - 1).add(new Edge(v, w));
                adj_list.get(v - 1).add(new Edge(u, w));
            }
        }

        int[] dist = dijkstra();

        for (int i = 0; i < n; i++) {
            int val = dist[i];
            if (val == Integer.MAX_VALUE) {
                System.out.println(-1);
            } else {
                System.out.println(val);
            }
        }
    }

    public static int[] dijkstra() {
        PriorityQueue<Edge> queue = new PriorityQueue<>();
        boolean[] visited = new boolean[n];
        int[] dist = new int[n];
        for (int i = 0; i < n; i++) {
            dist[i] = Integer.MAX_VALUE;
        }
        dist[0] = 0;
        queue.add(new Edge(1, 0));


        while (!queue.isEmpty()) {
            Edge v = queue.poll();
            visited[v.v - 1] = true;
            for (Edge neighbour : adj_list.get(v.v - 1)) {
                if (!visited[neighbour.v - 1]) {
                    int newDist = dist[v.v - 1] + neighbour.w;
                    if (newDist < dist[neighbour.v - 1]) {
                        dist[neighbour.v - 1] = newDist;
                        queue.add(new Edge(neighbour.v, dist[neighbour.v - 1]));
                    }
                }
            }
        }

        return dist;
    }

    static class Edge implements Comparable<Edge> {
        final int v;
        final int w;

        public Edge(int v, int w) {
            this.v = v;
            this.w = w;
        }

        public int compareTo(Edge v) {
            return this.w - v.w;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Edge edge = (Edge) o;
            return v == edge.v &&
                    w == edge.w;
        }

        @Override
        public int hashCode() {
            return Objects.hash(v, w);
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
